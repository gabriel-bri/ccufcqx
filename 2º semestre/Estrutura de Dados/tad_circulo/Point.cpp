#include <iostream>
#include <cmath>
#include "Point.h"

/****************************************
 * Implementacao das funcoes-membro
 ****************************************/
Point::Point() { 
    m_x = m_y = 0.0; 
}

Point::Point(double X, double Y) 
    : m_x(X), m_y(Y) { }

void Point::setX(double x) { 
    m_x = x; 
}

void Point::setY(double y) { 
    m_y = y; 
}

double Point::getX() { 
    return m_x; 
}

double Point::getY() { 
    return m_y; 
}

double Point::distance(const Point &p) {
    double dx = this->m_x - p.m_x;
    double dy = this->m_y - p.m_y;
    return sqrt(dx*dx + dy*dy);
}

void Point::print() { 
    std::cout << "Point(" << m_x << "," << m_y << ")"; 
}