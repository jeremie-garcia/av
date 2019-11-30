#ifndef IOCONFIG_H
#define IOCONFIG_H

#include <QWidget>

QT_BEGIN_NAMESPACE
namespace Ui { class IOConfig; }
QT_END_NAMESPACE

class IOConfig : public QWidget
{
    Q_OBJECT

public:
    IOConfig(QWidget *parent = nullptr);
    ~IOConfig();

private:
    Ui::IOConfig *ui;
};
#endif // IOCONFIG_H
