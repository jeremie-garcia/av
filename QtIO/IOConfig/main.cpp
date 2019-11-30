#include "ioconfig.h"

#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    IOConfig w;
    w.show();
    return a.exec();
}
