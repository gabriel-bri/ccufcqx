#ifndef PONTO_ED_2021
#define PONTO_ED_2021

/************************************
 * Declaracao da classe
 *************************************/
class Point {
private:
    double m_x, m_y;

public:
	// Construtor sem argumentos
    Point();

    // Construtor com dois argumentos
    Point(double X, double Y);
    
    // Setters
    void setX(double x);
    void setY(double y);
    
    // Getters
    double getX();
    double getY();
    
    // Calcula a distancia entre dois pontos
    double distance(const Point &p);
    
    // Imprime o ponto na tela
    void print();
};

#endif