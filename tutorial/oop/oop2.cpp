#include <iostream>
#include <iomanip>
#include <string>
#include <list>
#include <typeinfo>
using namespace std;


class Perro
{
  public:
    Perro()               { this->nombre = "";       this->edad = 0;      this->logct(1); }
    Perro(string nombre)  { this->nombre = nombre;   this->edad = 0;      this->logct(2); }
    Perro(int edad)       { this->nombre = "";       this->edad = edad;   this->logct(3); }
    Perro(string nombre, int edad)
                          { this->nombre = nombre;   this->edad = edad;   this->logct(4); }
    Perro(const Perro &o) { this->nombre = o.nombre; this->edad = o.edad; this->logct(); }
    ~Perro() { cout << "destructor de "; this->imprimir(); }

    virtual string getnombre() const { return this->nombre; }
    virtual void setnombre(string nombre) { this->nombre = nombre; }
    virtual int getedad() const { return this->edad; }
    virtual void setedad(int edad) { this->edad = edad; }

    virtual void imprimir() const { return this->imprimir(cout); }
    virtual void imprimir(ostream &out) const
    {
        out << setw(12) << right << this->clase() << ": ";
        out << this->getnombre() << "(" << this->getedad() << ")" << endl;
    }

  private:
    string nombre;
    int edad;

    const char *clase() const { return typeid(*this).name(); }
    void logct() const        { cout << "constructor de copia de "; this->imprimir(); }
    void logct(int n) const   { cout << "constructor " << n << " de "; this->imprimir(); }
};


int main()
{
    cout << "Inicio" << endl;

    Perro p1;
    Perro p2("cuki");
    Perro p3(7);
    Perro p4("pupi", 17);

    p1.imprimir();
    p2.imprimir();
    p3.imprimir();
    p3.setnombre("yupi");
    p3.imprimir();
    p4.imprimir();

    cout << "Lista" << endl;
    list<Perro> l = {p1, p2, p3, p4};
    for (std::list<Perro>::const_iterator it = l.begin(), end=l.end(); it != end; ++it)
    {
        it->imprimir();
    }

    cout << "Construccion y destruccion" << endl;
    Perro *p = new Perro("fufi", 2);
    {
        cout << "Entrando en interno" << endl;
        Perro interno(3);
        p->imprimir();
        delete p;
        interno.imprimir();
        cout << "Saliendo de interno" << endl;
    }
    //ojo: p->imprimir();

    cout << "Fin" << endl;
    return 0;
}
