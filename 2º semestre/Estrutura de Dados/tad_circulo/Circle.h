#ifndef CIRCLE_ED_2021
#define CIRCLE_ED_2021
#include "Point.h"

class Circle {
private:
    Point m_center;
    double m_radius;

public:
    // Construtor sem argumentos:
    // Inicializa o circulo como centro na origem (0,0)
    // e com raio igual a 1
    Circle();

    // Construtor com dois argumentos
    // Os dois argumentos sao obrigatorios
    Circle(Point& p, double rad);

    // setters
    void setRadius(double rad);
    void setCenter(Point& p);

    // getters
    Point& getCenter(); // Devolve uma referencia para m_center
    double getRadius(); // Devolve o valor de m_radius

    // Funcao-membro que devolve a area do circulo
    double area();

    // Funcao-membro que recebe um Point como argumento e
    // devolve 'true' se o ponto p estiver contido no circulo;
    // ou devolve 'false' caso contrario.
    bool contains(Point& p);
};

#endif