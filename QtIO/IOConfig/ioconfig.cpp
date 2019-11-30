#include "ioconfig.h"
#include "ui_ioconfig.h"

IOConfig::IOConfig(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::IOConfig)
{
    ui->setupUi(this);
}

IOConfig::~IOConfig()
{
    delete ui;
}

