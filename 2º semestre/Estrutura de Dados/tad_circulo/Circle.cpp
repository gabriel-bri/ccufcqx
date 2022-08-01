// Implementar
#include "Circle.h"
#include <iostream>
#include <math.h>       /* pow */
#include <cmath>       /* pow */

Circle::Circle() {
    this->m_center.setX(0);
    this->m_center.setY(0);
    this->setRadius(1);
}

Circle::Circle(Point& p, double rad) {
    this->setRadius(rad);
    this->m_center = p;
}

void Circle::setRadius(double rad) {
    this->m_radius = rad;
}

void Circle::setCenter(Point& p) {
    this->m_center = p;
}

Point& Circle::getCenter() {
    return this->m_center;
}

double Circle::getRadius() {
    return this->m_radius;
}

double Circle::area() {
    return  M_PI * pow(this->getRadius(), 2);
}

bool Circle::contains(Point& p) {
    return p.distance(this->m_center) < this->getRadius() ? true : false;
}