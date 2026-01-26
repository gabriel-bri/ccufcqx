#include <GL/glut.h>
#include <math.h>
#include <time.h>
#include <stdio.h>
#include <SFML/Audio.hpp>

sf::Music music;

// angulos dos ponteiros
float anguloHora = 0;
float anguloMinuto = 0;
float anguloSegundo = 0;

// camera
float angCamX = 0, angCamY = 0;
float dist = 15;
int mx, my;
int clicando = 0;

// pra pausar ou nao
int pausado = 0;

// ========== VARIÁVEIS PARA PICKING ==========
int corBorda = 0; // 0=madeira, 1=prateado, 2=dourado, 3=bronze, 4=cobre

// textura simples (array de pixels)
GLuint texturaRelogio;
GLuint texturaMadeira;

// funcao pra criar textura procedural de madeira
void criaTexturaMadeira() {
    const int TAM = 128;
    unsigned char textura[TAM][TAM][3];
    
    int i, j;
    for(i = 0; i < TAM; i++) {
        for(j = 0; j < TAM; j++) {
            // padrao de madeira com linhas
            float valor = sin(i * 0.2) * 0.3 + 0.7;
            textura[i][j][0] = (unsigned char)(101 * valor); // R
            textura[i][j][1] = (unsigned char)(67 * valor);  // G
            textura[i][j][2] = (unsigned char)(33 * valor);  // B
        }
    }
    
    glGenTextures(1, &texturaMadeira);
    glBindTexture(GL_TEXTURE_2D, texturaMadeira);
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, TAM, TAM, 0, GL_RGB, GL_UNSIGNED_BYTE, textura);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
}

// textura do mostrador do relogio (numeros romanos simplificados)
void criaTexturaRelogio() {
    const int TAM = 256;
    unsigned char textura[TAM][TAM][3];
    
    int i, j;
    // fundo branco
    for(i = 0; i < TAM; i++) {
        for(j = 0; j < TAM; j++) {
            textura[i][j][0] = 245;
            textura[i][j][1] = 245;
            textura[i][j][2] = 240;
        }
    }
    
    // desenha algumas marcacoes (linhas radiais)
    int centro = TAM / 2;
    int k;
    for(k = 0; k < 12; k++) {
        float angulo = k * 3.14159 * 2.0 / 12.0;
        int raio = TAM / 2 - 10;
        
        for(int r = raio - 15; r < raio; r++) {
            int x = centro + (int)(r * cos(angulo));
            int y = centro + (int)(r * sin(angulo));
            
            if(x >= 0 && x < TAM && y >= 0 && y < TAM) {
                // marcacao mais grossa nas horas principais
                int espessura = (k % 3 == 0) ? 3 : 1;
                for(int dx = -espessura; dx <= espessura; dx++) {
                    for(int dy = -espessura; dy <= espessura; dy++) {
                        int nx = x + dx;
                        int ny = y + dy;
                        if(nx >= 0 && nx < TAM && ny >= 0 && ny < TAM) {
                            textura[nx][ny][0] = 20;
                            textura[nx][ny][1] = 20;
                            textura[nx][ny][2] = 20;
                        }
                    }
                }
            }
        }
    }
    
    glGenTextures(1, &texturaRelogio);
    glBindTexture(GL_TEXTURE_2D, texturaRelogio);
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, TAM, TAM, 0, GL_RGB, GL_UNSIGNED_BYTE, textura);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
}

void tocarSom() {
    if (!music.openFromFile("pendulo.wav")) {
        printf("Erro ao abrir pendulo.wav\n");
        return;
    }
    
    music.setLooping(true);
    music.play();
}

void pararSom() {
    music.stop();
}

void atualizaHora() {
    if(pausado) return;
    
    time_t agora;
    struct tm *info;
    
    time(&agora);
    info = localtime(&agora);
    
    int h = info->tm_hour;
    int m = info->tm_min;
    int s = info->tm_sec;
    
    anguloSegundo = -s * 6.0;
    anguloMinuto = -m * 6.0 - s * 0.1;
    anguloHora = -(h % 12) * 30.0 - m * 0.5;
}

// verifica se é dia ou noite
int ehDia() {
    time_t agora;
    struct tm *info;
    time(&agora);
    info = localtime(&agora);
    int h = info->tm_hour;
    return (h >= 6 && h < 18); // dia entre 6h e 18h
}

// ajusta cor do fundo baseado na hora
void ajustaCorFundo() {
    time_t agora;
    struct tm *info;
    time(&agora);
    info = localtime(&agora);
    int h = info->tm_hour;
    
    float r, g, b;
    
    if(h >= 6 && h < 18) {
        // dia - cinza claro azulado
        r = 0.85f;
        g = 0.85f;
        b = 0.9f;
    } else {
        // noite - preto azulado escuro
        r = 0.05f;
        g = 0.05f;
        b = 0.15f;
    }
    
    glClearColor(r, g, b, 1.0f);
}

// desenha sol no canto superior esquerdo
void desenhaSol() {
    glDisable(GL_LIGHTING); // desliga luz pra cores ficarem vivas
    
    glPushMatrix();
    glTranslatef(-8, 6, -5);
    
    // corpo do sol amarelo
    glColor3f(1.0, 0.9, 0.1);
    glutSolidSphere(1.2, 20, 20);
    
    // raios do sol
    glColor3f(1.0, 0.8, 0.0);
    int i;
    for(i = 0; i < 8; i++) {
        glPushMatrix();
        glRotatef(i * 45, 0, 0, 1);
        glTranslatef(0, 1.8, 0);
        glScalef(0.15, 0.8, 0.15);
        glutSolidCube(1);
        glPopMatrix();
    }
    
    glPopMatrix();
    
    glEnable(GL_LIGHTING);
}

// desenha lua no canto superior esquerdo
void desenhaLua() {
    glDisable(GL_LIGHTING);
    
    glPushMatrix();
    glTranslatef(-8, 6, -5);
    
    // lua cinza clara
    glColor3f(0.9, 0.9, 0.85);
    glutSolidSphere(1.0, 20, 20);
    
    // crateras (esferas menores mais escuras)
    glColor3f(0.7, 0.7, 0.65);
    glPushMatrix();
    glTranslatef(0.3, 0.4, 0.8);
    glutSolidSphere(0.2, 10, 10);
    glPopMatrix();
    
    glPushMatrix();
    glTranslatef(-0.4, -0.2, 0.9);
    glutSolidSphere(0.15, 10, 10);
    glPopMatrix();
    
    glPushMatrix();
    glTranslatef(0.2, -0.5, 0.85);
    glutSolidSphere(0.18, 10, 10);
    glPopMatrix();
    
    // estrelinhas ao redor
    glColor3f(1.0, 1.0, 0.9);
    int i;
    for(i = 0; i < 5; i++) {
        glPushMatrix();
        float ang = i * 3.14159 * 2.0 / 5.0;
        glTranslatef(2.5 * cos(ang), 2.5 * sin(ang), -1);
        glutSolidSphere(0.1, 8, 8);
        glPopMatrix();
    }
    
    glPopMatrix();
    
    glEnable(GL_LIGHTING);
}

// desenha o corpo do relogio COM TEXTURA
void desenhaCorpo() {
    glEnable(GL_TEXTURE_2D);
    glBindTexture(GL_TEXTURE_2D, texturaRelogio);
    
    // circulo de fundo com textura
    glColor3f(1, 1, 1); // branco pra nao alterar a textura
    
    GLUquadric *quad = gluNewQuadric();
    gluQuadricTexture(quad, GL_TRUE);
    gluQuadricNormals(quad, GLU_SMOOTH);
    
    glPushMatrix();
    gluDisk(quad, 0, 4, 40, 1);
    glPopMatrix();
    
    gluDeleteQuadric(quad);
    glDisable(GL_TEXTURE_2D);
    
    // borda do relogio - MUDA COR BASEADO NA SELEÇÃO
    glDisable(GL_TEXTURE_2D);
    
    switch(corBorda) {
        case 0: // madeira original
            glEnable(GL_TEXTURE_2D);
            glBindTexture(GL_TEXTURE_2D, texturaMadeira);
            glColor3f(1, 1, 1);
            break;
        case 1: // prateado
            glColor3f(0.75, 0.75, 0.8);
            break;
        case 2: // dourado
            glColor3f(1.0, 0.84, 0.0);
            break;
        case 3: // bronze
            glColor3f(0.8, 0.5, 0.2);
            break;
        case 4: // cobre/rose gold
            glColor3f(0.72, 0.45, 0.20);
            break;
    }
    
    glPushMatrix();
    glutSolidTorus(0.4, 4.3, 20, 40);
    glPopMatrix();
    
    glDisable(GL_TEXTURE_2D);
    
    // pontinho no centro
    glColor3f(0.2, 0.2, 0.2);
    glPushMatrix();
    glTranslatef(0, 0, 0.5);
    glutSolidSphere(0.2, 10, 10);
    glPopMatrix();
}

// ponteiro das horas (curto e grosso)
void desenhaPonteiroHora() {
    glColor3f(0.1, 0.1, 0.1);
    glPushMatrix();
    glRotatef(anguloHora, 0, 0, 1);
    glTranslatef(0, 1.2, 0.5);
    glScalef(0.15, 2.4, 0.1);
    glutSolidCube(1);
    glPopMatrix();
}

// ponteiro dos minutos (medio)
void desenhaPonteiroMinuto() {
    glColor3f(0.15, 0.15, 0.15);
    glPushMatrix();
    glRotatef(anguloMinuto, 0, 0, 1);
    glTranslatef(0, 1.8, 0.52);
    glScalef(0.12, 3.6, 0.08);
    glutSolidCube(1);
    glPopMatrix();
}

// ponteiro dos segundos (fino e vermelho)
void desenhaPonteiroSegundo() {
    glColor3f(0.8, 0.1, 0.1);
    glPushMatrix();
    glRotatef(anguloSegundo, 0, 0, 1);
    glTranslatef(0, 2, 0.54);
    glScalef(0.08, 4, 0.06);
    glutSolidCube(1);
    glPopMatrix();
}

// pendulo com textura de madeira
void desenhaPendulo() {
    glEnable(GL_TEXTURE_2D);
    glBindTexture(GL_TEXTURE_2D, texturaMadeira);
    glColor3f(1, 1, 1);
    
    // haste
    glPushMatrix();
    glTranslatef(0, -1.5, 0);
    float balanco = sin(anguloSegundo * 0.1) * 15;
    glRotatef(balanco, 0, 0, 1);
    glTranslatef(0, -2, 0);
    glScalef(0.08, 4, 0.08);
    glutSolidCube(1);
    glPopMatrix();
    
    glDisable(GL_TEXTURE_2D);
    
    // peso na ponta (dourado)
    glColor3f(0.8, 0.7, 0.2);
    glPushMatrix();
    glTranslatef(0, -1.5, 0);
    glRotatef(balanco, 0, 0, 1);
    glTranslatef(0, -4, 0);
    glutSolidSphere(0.4, 12, 12);
    glPopMatrix();
}

// ========== NOVAS FUNÇÕES DE SOMBRA ==========

// desenha um chão simples para receber as sombras
void desenhaChao() {
    glDisable(GL_LIGHTING);
    glColor3f(0.4, 0.4, 0.4);
    
    glBegin(GL_QUADS);
    glVertex3f(-15, -7, -15);
    glVertex3f(15, -7, -15);
    glVertex3f(15, -7, 15);
    glVertex3f(-15, -7, 15);
    glEnd();
    
    glEnable(GL_LIGHTING);
}

// sombra dos ponteiros projetada no mostrador do relógio
void desenhaSombraPonteiros() {
    // desabilita iluminação e habilita transparência
    glDisable(GL_LIGHTING);
    glEnable(GL_BLEND);
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
    
    // cor da sombra (preto semi-transparente)
    glColor4f(0, 0, 0, 0.25);
    
    // desloca um pouco para simular projeção da luz
    glPushMatrix();
    glTranslatef(0.3, -0.3, 0.02); // offset da posição da luz
    
    // redesenha os ponteiros (agora como sombra)
    glPushMatrix();
    glRotatef(anguloHora, 0, 0, 1);
    glTranslatef(0, 1.2, 0);
    glScalef(0.15, 2.4, 0.01); // mais achatado em Z
    glutSolidCube(1);
    glPopMatrix();
    
    glPushMatrix();
    glRotatef(anguloMinuto, 0, 0, 1);
    glTranslatef(0, 1.8, 0);
    glScalef(0.12, 3.6, 0.01);
    glutSolidCube(1);
    glPopMatrix();
    
    glPushMatrix();
    glRotatef(anguloSegundo, 0, 0, 1);
    glTranslatef(0, 2, 0);
    glScalef(0.08, 4, 0.01);
    glutSolidCube(1);
    glPopMatrix();
    
    glPopMatrix();
    
    // restaura configurações
    glDisable(GL_BLEND);
    glEnable(GL_LIGHTING);
}

// sombra do pêndulo projetada no chão
void desenhaSombraPendulo() {
    glDisable(GL_LIGHTING);
    glEnable(GL_BLEND);
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
    
    glColor4f(0, 0, 0, 0.3);
    
    float balanco = sin(anguloSegundo * 0.1) * 15;
    
    // calcula posição do peso do pêndulo
    float pendX = sin(balanco * 3.14159 / 180.0) * 4.0;
    float pendY = -5.5 - cos(balanco * 3.14159 / 180.0) * 4.0;
    
    glPushMatrix();
    
    // desenha linha da haste (do centro até o peso)
    glBegin(GL_QUADS);
    float largura = 0.15;
    // offset da luz
    float offsetX = 0.5;
    float offsetY = -0.3;
    
    glVertex3f(offsetX - largura, -1.5 + offsetY, 0.01);
    glVertex3f(offsetX + largura, -1.5 + offsetY, 0.01);
    glVertex3f(pendX + offsetX + largura, pendY + offsetY, 0.01);
    glVertex3f(pendX + offsetX - largura, pendY + offsetY, 0.01);
    glEnd();
    
    // desenha sombra do peso (círculo achatado)
    glTranslatef(pendX + offsetX, -7, 0.02);
    
    GLUquadric *quad = gluNewQuadric();
    gluDisk(quad, 0, 0.5, 20, 1);
    gluDeleteQuadric(quad);
    
    glPopMatrix();
    
    glDisable(GL_BLEND);
    glEnable(GL_LIGHTING);
}

// sombra do corpo do relógio no chão
void desenhaSombraRelogio() {
    glDisable(GL_LIGHTING);
    glEnable(GL_BLEND);
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
    
    glColor4f(0, 0, 0, 0.35);
    
    glPushMatrix();
    
    // projeta no chão
    glTranslatef(1, -7, 0.02); // offset da luz
    
    // desenha elipse achatada
    glScalef(1.2, 0.01, 1); // achata e aumenta um pouco
    
    GLUquadric *quad = gluNewQuadric();
    gluDisk(quad, 0, 4.5, 40, 1);
    gluDeleteQuadric(quad);
    
    glPopMatrix();
    
    glDisable(GL_BLEND);
    glEnable(GL_LIGHTING);
}

// ========== FIM DAS FUNÇÕES DE SOMBRA ==========

// ========== FUNÇÕES DE PICKING ==========

// desenha apenas a borda com nome (ID) para picking
void desenhaBordaComNome() {
    // borda do relógio (ID = 1)
    glLoadName(1); // usa LoadName em vez de PushName pois já temos um nome na pilha
    glPushMatrix();
    glutSolidTorus(0.4, 4.3, 20, 40);
    glPopMatrix();
}

// realiza picking na posição do mouse
int realizaPicking(int x, int y) {
    GLuint selectBuf[512];
    GLint viewport[4];
    
    // pega dimensões da janela
    int largura = glutGet(GLUT_WINDOW_WIDTH);
    int altura = glutGet(GLUT_WINDOW_HEIGHT);
    
    // configura viewport para picking (tela cheia)
    viewport[0] = 0;
    viewport[1] = 0;
    viewport[2] = largura;
    viewport[3] = altura;
    
    glSelectBuffer(512, selectBuf);
    glRenderMode(GL_SELECT);
    
    glInitNames();
    glPushName(0);
    
    glMatrixMode(GL_PROJECTION);
    glPushMatrix();
    glLoadIdentity();
    
    // aumenta região de picking para 10x10 pixels
    gluPickMatrix(x, viewport[3] - y, 10.0, 10.0, viewport);
    gluPerspective(45, (float)largura / altura, 0.1, 100);
    
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    
    // configura camera (igual ao display)
    float cx = dist * sin(angCamY * 3.14/180) * cos(angCamX * 3.14/180);
    float cy = dist * sin(angCamX * 3.14/180);
    float cz = dist * cos(angCamY * 3.14/180) * cos(angCamX * 3.14/180);
    gluLookAt(cx, cy, cz, 0, 0, 0, 0, 1, 0);
    
    // desenha apenas a borda com nome
    desenhaBordaComNome();
    
    glMatrixMode(GL_PROJECTION);
    glPopMatrix();
    glMatrixMode(GL_MODELVIEW);
    
    GLint hits = glRenderMode(GL_RENDER);
    
    // processa hits
    if(hits > 0) {
        // pega o objeto mais próximo (menor Z)
        GLuint minZ = selectBuf[1];
        int objetoSelecionado = selectBuf[3];
        
        for(int i = 1; i < hits; i++) {
            if(selectBuf[i * 4 + 1] < minZ) {
                minZ = selectBuf[i * 4 + 1];
                objetoSelecionado = selectBuf[i * 4 + 3];
            }
        }
        
        return objetoSelecionado;
    }
    
    return 0; // nenhum objeto selecionado
}

// ========== FIM DAS FUNÇÕES DE PICKING ==========

void display() {
    // atualiza cor de fundo baseado na hora
    ajustaCorFundo();
    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    
    // ajusta intensidade da luz baseado no horario
    time_t agora;
    struct tm *info;
    time(&agora);
    info = localtime(&agora);
    int h = info->tm_hour;
    
    float intensidade = (h >= 6 && h < 18) ? 0.8f : 0.3f;
    GLfloat posLuz[] = {5, 5, 10, 1};
    GLfloat difusa[] = {intensidade, intensidade, intensidade, 1};
    glLightfv(GL_LIGHT0, GL_DIFFUSE, difusa);
    glLightfv(GL_LIGHT0, GL_POSITION, posLuz);
    
    int largura = glutGet(GLUT_WINDOW_WIDTH);
    int altura = glutGet(GLUT_WINDOW_HEIGHT);
    
    // ========== VIEWPORT PRINCIPAL (tela cheia) ==========
    glViewport(0, 0, largura, altura);
    
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluPerspective(45, (float)largura / altura, 0.1, 100);
    
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    
    // posiciona camera principal (controlada pelo mouse)
    float cx = dist * sin(angCamY * 3.14/180) * cos(angCamX * 3.14/180);
    float cy = dist * sin(angCamX * 3.14/180);
    float cz = dist * cos(angCamY * 3.14/180) * cos(angCamX * 3.14/180);
    gluLookAt(cx, cy, cz, 0, 0, 0, 0, 1, 0);
    
    // desenha cena completa
    if(ehDia()) {
        desenhaSol();
    } else {
        desenhaLua();
    }
    
    desenhaChao();
    desenhaSombraRelogio();
    desenhaSombraPendulo();
    desenhaCorpo();
    desenhaSombraPonteiros();
    desenhaPonteiroHora();
    desenhaPonteiroMinuto();
    desenhaPonteiroSegundo();
    desenhaPendulo();
    
    // ========== VIEWPORT SECUNDÁRIA (mini - canto superior direito) ==========
    int miniLargura = largura / 4;  // 25% da largura
    int miniAltura = altura / 4;     // 25% da altura
    
    glViewport(largura - miniLargura, altura - miniAltura, miniLargura, miniAltura);
    
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluPerspective(45, (float)miniLargura / miniAltura, 0.1, 100);
    
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    
    // câmera fixa - visão frontal
    gluLookAt(0, 0, 15, 0, 0, 0, 0, 1, 0);
    
    // limpa apenas a área da mini viewport
    glScissor(largura - miniLargura, altura - miniAltura, miniLargura, miniAltura);
    glEnable(GL_SCISSOR_TEST);
    glClear(GL_DEPTH_BUFFER_BIT);
    glDisable(GL_SCISSOR_TEST);
    
    // desenha cena novamente (visão frontal fixa)
    if(ehDia()) {
        desenhaSol();
    } else {
        desenhaLua();
    }
    
    desenhaChao();
    desenhaSombraRelogio();
    desenhaSombraPendulo();
    desenhaCorpo();
    desenhaSombraPonteiros();
    desenhaPonteiroHora();
    desenhaPonteiroMinuto();
    desenhaPonteiroSegundo();
    desenhaPendulo();
    
    // desenha borda branca ao redor da mini viewport
    glDisable(GL_LIGHTING);
    glDisable(GL_DEPTH_TEST);
    
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    glOrtho(0, miniLargura, 0, miniAltura, -1, 1);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    
    glColor3f(1, 1, 1);
    glLineWidth(2);
    glBegin(GL_LINE_LOOP);
    glVertex2f(2, 2);
    glVertex2f(miniLargura - 2, 2);
    glVertex2f(miniLargura - 2, miniAltura - 2);
    glVertex2f(2, miniAltura - 2);
    glEnd();
    glLineWidth(1);
    
    glEnable(GL_DEPTH_TEST);
    glEnable(GL_LIGHTING);
    
    glutSwapBuffers();
}

void timer(int v) {
    atualizaHora();
    glutPostRedisplay();
    glutTimerFunc(50, timer, 0);
}

void reshape(int w, int h) {
    if(h == 0) h = 1;
    glViewport(0, 0, w, h);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluPerspective(45, (float)w/h, 0.1, 100);
    glMatrixMode(GL_MODELVIEW);
}

void teclado(unsigned char k, int x, int y) {
    if(k == 27) exit(0);
    if(k == ' ') pausado = !pausado;
    if(k == '+' || k == '=') {
        dist -= 1;
        if(dist < 8) dist = 8;
    }
    
    if(k == 'p'){
        tocarSom();     
    }
    
    if(k == 's'){
        pararSom();
    }

    if(k == '-') {
        dist += 1;
        if(dist > 30) dist = 30;
    }
    glutPostRedisplay();
}

void mouse(int botao, int estado, int x, int y) {
    if(botao == GLUT_LEFT_BUTTON && estado == GLUT_DOWN) {
        // tenta fazer picking primeiro
        int objetoClicado = realizaPicking(x, y);
        
        if(objetoClicado == 1) {
            // clicou na borda - cicla entre as cores
            corBorda = (corBorda + 1) % 5; // 0 a 4
            
            switch(corBorda) {
                case 0: printf("Borda: MADEIRA\n"); break;
                case 1: printf("Borda: PRATEADO\n"); break;
                case 2: printf("Borda: DOURADO\n"); break;
                case 3: printf("Borda: BRONZE\n"); break;
                case 4: printf("Borda: COBRE\n"); break;
            }
            
            glutPostRedisplay();
        } else {
            // não clicou na borda, inicia rotação da câmera
            clicando = 1;
            mx = x;
            my = y;
        }
    }
    if(botao == GLUT_LEFT_BUTTON && estado == GLUT_UP) {
        clicando = 0;
    }
    
    // clique direito volta para madeira original
    if(botao == GLUT_RIGHT_BUTTON && estado == GLUT_DOWN) {
        if(corBorda != 0) {
            corBorda = 0;
            printf("Borda: MADEIRA (resetado)\n");
            glutPostRedisplay();
        }
    }
}

void movimento(int x, int y) {
    if(clicando) {
        angCamY += (x - mx) * 0.5;
        angCamX += (y - my) * 0.5;
        
        if(angCamX > 85) angCamX = 85;
        if(angCamX < -85) angCamX = -85;
        
        mx = x;
        my = y;
        glutPostRedisplay();
    }
}

void init() {
    // cor inicial (vai ser ajustada no display)
    glClearColor(0.85, 0.85, 0.9, 1);
    glEnable(GL_DEPTH_TEST);
    glEnable(GL_LIGHTING);
    glEnable(GL_LIGHT0);
    glEnable(GL_COLOR_MATERIAL);
    glShadeModel(GL_SMOOTH);
    
    // luz ambiente
    GLfloat ambiente[] = {0.4, 0.4, 0.4, 1};
    GLfloat difusa[] = {0.8, 0.8, 0.8, 1};
    GLfloat especular[] = {0.3, 0.3, 0.3, 1};
    
    glLightfv(GL_LIGHT0, GL_AMBIENT, ambiente);
    glLightfv(GL_LIGHT0, GL_DIFFUSE, difusa);
    glLightfv(GL_LIGHT0, GL_SPECULAR, especular);
    
    // cria texturas procedurais
    criaTexturaRelogio();
    criaTexturaMadeira();
    
    atualizaHora();
}

int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
    glutInitWindowSize(900, 700);
    glutCreateWindow("Relogio 3D");
    
    init();
    
    glutDisplayFunc(display);
    glutReshapeFunc(reshape);
    glutKeyboardFunc(teclado);
    glutMouseFunc(mouse);
    glutMotionFunc(movimento);
    glutTimerFunc(50, timer, 0);
    
    printf("Mouse: rotaciona camera\n");
    printf("Clique ESQUERDO na borda: cicla entre cores\n");
    printf(" MADEIRA > PRATEADO > DOURADO > BRONZE > COBRE\n");
    printf("Clique DIREITO: volta para madeira original\n");
    printf("Espaco: pausa/despausa\n");
    printf("+/- : zoom\n");
    printf("P: tocar som pendulo\n");
    printf("S: parar som\n");
    printf("ESC: sair\n");
    printf("\nSol aparece de dia (6h-18h)\n");
    printf("Lua aparece de noite (18h-6h)\n");   
    glutMainLoop();
    return 0;
}
