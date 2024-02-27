#include <iostream>
#include <iomanip>
#include <string>
#include <list>
#include <typeinfo>
using namespace std;


class Animal
{
  public:
    virtual const string hazruido() const { return "ruido animal"; }
    virtual const string operator+(int) const { return this->hazruido() + " entero"; }
    virtual const string operator+(double) const { return this->hazruido() + " real"; }
    int dametamano() const { return 0; }
    int dametamano(string) const { return 2; }
};

class Perro: public Animal
{
  public:
    virtual const string hazruido() const { return "guau"; }
    virtual const string operator+(double) const { return this->hazruido() + " chucho"; }
    int dametamano() const { return 10; }
};

class Gato: public Animal
{
  public:
    virtual const string hazruido() const { return "miau"; }
    int dametamano() const { return 4; }
};

class Doberman: public Perro
{
  public:
    virtual const string hazruido() const { return "grrrrr"; }
    int dametamano() const { return 20; }
    int dametamano(string) const { return 17; }
};

const char *clase(const Animal &a) { return typeid(a).name(); }


void ver_bicho(const Animal &a)
{
    cout << setw(12) << right << clase(a) << ": ";
    cout << a.hazruido() << "(" << a.dametamano() << ")" << endl;
}


int main()
{
    cout << "Inicio" << endl;

    Animal a = Animal();
    Perro p;
    Gato g;
    Doberman d;

    ver_bicho(a);
    ver_bicho(p);
    ver_bicho(g);
    ver_bicho(d);

    cout << "Lista" << endl;
    list<Animal> l = {a, p, g, d};
    for (std::list<Animal>::const_iterator it = l.begin(), end=l.end(); it != end; ++it)
    {
        ver_bicho(*it);
    }

    cout << "Sobrecarga" << endl;
    string se = a + 34;
    string sf = a + 4.2;
    cout << setw(12) << right << clase(a) << ": ";
    cout << se << " y " << sf << endl;
    string de = d + 34;
    string df = d + 4.2;
    cout << setw(12) << right << clase(d) << ": ";
    cout << de << " y " << df << endl;
    cout << setw(12) << right << clase(d) << ": ";
    cout << d.dametamano("raro") << endl;

    cout << "Fin" << endl;
    return 0;
}
