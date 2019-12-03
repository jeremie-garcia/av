/********************************************************************************
** Form generated from reading UI file 'ioconfig.ui'
**
** Created by: Qt User Interface Compiler version 5.12.6
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_IOCONFIG_H
#define UI_IOCONFIG_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QCheckBox>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QFrame>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QToolButton>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_IOConfig
{
public:
    QGridLayout *gridLayout;
    QVBoxLayout *genVertLay;
    QVBoxLayout *assiVertLay;
    QFrame *line_4;
    QLabel *assiLabel;
    QFrame *line_3;
    QGridLayout *assiGridLay;
    QComboBox *outputCombo;
    QToolButton *delAssiButton;
    QLabel *sortielabel;
    QToolButton *addAssiButton;
    QLabel *entreelabel;
    QComboBox *inputCombo;
    QCheckBox *checkBox;
    QLabel *label;
    QVBoxLayout *varVertLay;
    QFrame *line;
    QLabel *varLabel;
    QFrame *line_2;
    QGridLayout *varGridLay;
    QToolButton *addVarButton;
    QLabel *valeurLabel;
    QComboBox *typeCombo;
    QLabel *typeLabel;
    QLineEdit *valeurLine;
    QToolButton *delVarButton;
    QLabel *nomLabel;
    QLineEdit *nomLine;
    QHBoxLayout *buttonHorLay;
    QPushButton *annulerButton;
    QPushButton *enregistrerButton;
    QPushButton *validerButton;

    void setupUi(QWidget *IOConfig)
    {
        if (IOConfig->objectName().isEmpty())
            IOConfig->setObjectName(QString::fromUtf8("IOConfig"));
        IOConfig->resize(503, 305);
        QSizePolicy sizePolicy(QSizePolicy::Fixed, QSizePolicy::Fixed);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(IOConfig->sizePolicy().hasHeightForWidth());
        IOConfig->setSizePolicy(sizePolicy);
        IOConfig->setWindowOpacity(1.000000000000000);
        gridLayout = new QGridLayout(IOConfig);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        genVertLay = new QVBoxLayout();
        genVertLay->setObjectName(QString::fromUtf8("genVertLay"));
        assiVertLay = new QVBoxLayout();
        assiVertLay->setObjectName(QString::fromUtf8("assiVertLay"));
        line_4 = new QFrame(IOConfig);
        line_4->setObjectName(QString::fromUtf8("line_4"));
        line_4->setFrameShape(QFrame::HLine);
        line_4->setFrameShadow(QFrame::Sunken);

        assiVertLay->addWidget(line_4);

        assiLabel = new QLabel(IOConfig);
        assiLabel->setObjectName(QString::fromUtf8("assiLabel"));
        QSizePolicy sizePolicy1(QSizePolicy::Preferred, QSizePolicy::Maximum);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(assiLabel->sizePolicy().hasHeightForWidth());
        assiLabel->setSizePolicy(sizePolicy1);
        assiLabel->setAlignment(Qt::AlignCenter);

        assiVertLay->addWidget(assiLabel);

        line_3 = new QFrame(IOConfig);
        line_3->setObjectName(QString::fromUtf8("line_3"));
        line_3->setFrameShape(QFrame::HLine);
        line_3->setFrameShadow(QFrame::Sunken);

        assiVertLay->addWidget(line_3);

        assiGridLay = new QGridLayout();
        assiGridLay->setObjectName(QString::fromUtf8("assiGridLay"));
        assiGridLay->setSizeConstraint(QLayout::SetDefaultConstraint);
        outputCombo = new QComboBox(IOConfig);
        outputCombo->setObjectName(QString::fromUtf8("outputCombo"));

        assiGridLay->addWidget(outputCombo, 1, 2, 1, 1);

        delAssiButton = new QToolButton(IOConfig);
        delAssiButton->setObjectName(QString::fromUtf8("delAssiButton"));

        assiGridLay->addWidget(delAssiButton, 1, 3, 1, 1);

        sortielabel = new QLabel(IOConfig);
        sortielabel->setObjectName(QString::fromUtf8("sortielabel"));
        sizePolicy1.setHeightForWidth(sortielabel->sizePolicy().hasHeightForWidth());
        sortielabel->setSizePolicy(sizePolicy1);
        sortielabel->setAlignment(Qt::AlignCenter);

        assiGridLay->addWidget(sortielabel, 0, 2, 1, 1);

        addAssiButton = new QToolButton(IOConfig);
        addAssiButton->setObjectName(QString::fromUtf8("addAssiButton"));

        assiGridLay->addWidget(addAssiButton, 2, 3, 1, 1);

        entreelabel = new QLabel(IOConfig);
        entreelabel->setObjectName(QString::fromUtf8("entreelabel"));
        sizePolicy1.setHeightForWidth(entreelabel->sizePolicy().hasHeightForWidth());
        entreelabel->setSizePolicy(sizePolicy1);
        entreelabel->setAlignment(Qt::AlignCenter);

        assiGridLay->addWidget(entreelabel, 0, 1, 1, 1);

        inputCombo = new QComboBox(IOConfig);
        inputCombo->setObjectName(QString::fromUtf8("inputCombo"));

        assiGridLay->addWidget(inputCombo, 1, 1, 1, 1);

        checkBox = new QCheckBox(IOConfig);
        checkBox->setObjectName(QString::fromUtf8("checkBox"));
        QSizePolicy sizePolicy2(QSizePolicy::Maximum, QSizePolicy::Fixed);
        sizePolicy2.setHorizontalStretch(0);
        sizePolicy2.setVerticalStretch(0);
        sizePolicy2.setHeightForWidth(checkBox->sizePolicy().hasHeightForWidth());
        checkBox->setSizePolicy(sizePolicy2);
        checkBox->setLayoutDirection(Qt::LeftToRight);
        checkBox->setChecked(false);
        checkBox->setTristate(false);

        assiGridLay->addWidget(checkBox, 1, 0, 1, 1, Qt::AlignHCenter);

        label = new QLabel(IOConfig);
        label->setObjectName(QString::fromUtf8("label"));
        QSizePolicy sizePolicy3(QSizePolicy::Maximum, QSizePolicy::Preferred);
        sizePolicy3.setHorizontalStretch(0);
        sizePolicy3.setVerticalStretch(0);
        sizePolicy3.setHeightForWidth(label->sizePolicy().hasHeightForWidth());
        label->setSizePolicy(sizePolicy3);
        label->setAlignment(Qt::AlignCenter);

        assiGridLay->addWidget(label, 0, 0, 1, 1);


        assiVertLay->addLayout(assiGridLay);


        genVertLay->addLayout(assiVertLay);

        varVertLay = new QVBoxLayout();
        varVertLay->setObjectName(QString::fromUtf8("varVertLay"));
        line = new QFrame(IOConfig);
        line->setObjectName(QString::fromUtf8("line"));
        line->setFrameShape(QFrame::HLine);
        line->setFrameShadow(QFrame::Sunken);

        varVertLay->addWidget(line);

        varLabel = new QLabel(IOConfig);
        varLabel->setObjectName(QString::fromUtf8("varLabel"));
        sizePolicy1.setHeightForWidth(varLabel->sizePolicy().hasHeightForWidth());
        varLabel->setSizePolicy(sizePolicy1);
        varLabel->setAlignment(Qt::AlignCenter);

        varVertLay->addWidget(varLabel);

        line_2 = new QFrame(IOConfig);
        line_2->setObjectName(QString::fromUtf8("line_2"));
        line_2->setFrameShape(QFrame::HLine);
        line_2->setFrameShadow(QFrame::Sunken);

        varVertLay->addWidget(line_2);

        varGridLay = new QGridLayout();
        varGridLay->setObjectName(QString::fromUtf8("varGridLay"));
        addVarButton = new QToolButton(IOConfig);
        addVarButton->setObjectName(QString::fromUtf8("addVarButton"));

        varGridLay->addWidget(addVarButton, 2, 3, 1, 1, Qt::AlignHCenter);

        valeurLabel = new QLabel(IOConfig);
        valeurLabel->setObjectName(QString::fromUtf8("valeurLabel"));
        sizePolicy1.setHeightForWidth(valeurLabel->sizePolicy().hasHeightForWidth());
        valeurLabel->setSizePolicy(sizePolicy1);
        valeurLabel->setAlignment(Qt::AlignCenter);

        varGridLay->addWidget(valeurLabel, 0, 2, 1, 1);

        typeCombo = new QComboBox(IOConfig);
        typeCombo->setObjectName(QString::fromUtf8("typeCombo"));

        varGridLay->addWidget(typeCombo, 1, 1, 1, 1);

        typeLabel = new QLabel(IOConfig);
        typeLabel->setObjectName(QString::fromUtf8("typeLabel"));
        sizePolicy1.setHeightForWidth(typeLabel->sizePolicy().hasHeightForWidth());
        typeLabel->setSizePolicy(sizePolicy1);
        typeLabel->setAlignment(Qt::AlignCenter);

        varGridLay->addWidget(typeLabel, 0, 1, 1, 1);

        valeurLine = new QLineEdit(IOConfig);
        valeurLine->setObjectName(QString::fromUtf8("valeurLine"));

        varGridLay->addWidget(valeurLine, 1, 2, 1, 1);

        delVarButton = new QToolButton(IOConfig);
        delVarButton->setObjectName(QString::fromUtf8("delVarButton"));

        varGridLay->addWidget(delVarButton, 1, 3, 1, 1);

        nomLabel = new QLabel(IOConfig);
        nomLabel->setObjectName(QString::fromUtf8("nomLabel"));
        sizePolicy1.setHeightForWidth(nomLabel->sizePolicy().hasHeightForWidth());
        nomLabel->setSizePolicy(sizePolicy1);
        nomLabel->setAlignment(Qt::AlignCenter);

        varGridLay->addWidget(nomLabel, 0, 0, 1, 1);

        nomLine = new QLineEdit(IOConfig);
        nomLine->setObjectName(QString::fromUtf8("nomLine"));

        varGridLay->addWidget(nomLine, 1, 0, 1, 1);


        varVertLay->addLayout(varGridLay);


        genVertLay->addLayout(varVertLay);

        buttonHorLay = new QHBoxLayout();
        buttonHorLay->setObjectName(QString::fromUtf8("buttonHorLay"));
        buttonHorLay->setSizeConstraint(QLayout::SetDefaultConstraint);
        annulerButton = new QPushButton(IOConfig);
        annulerButton->setObjectName(QString::fromUtf8("annulerButton"));
        QSizePolicy sizePolicy4(QSizePolicy::Minimum, QSizePolicy::Maximum);
        sizePolicy4.setHorizontalStretch(0);
        sizePolicy4.setVerticalStretch(0);
        sizePolicy4.setHeightForWidth(annulerButton->sizePolicy().hasHeightForWidth());
        annulerButton->setSizePolicy(sizePolicy4);

        buttonHorLay->addWidget(annulerButton);

        enregistrerButton = new QPushButton(IOConfig);
        enregistrerButton->setObjectName(QString::fromUtf8("enregistrerButton"));
        sizePolicy4.setHeightForWidth(enregistrerButton->sizePolicy().hasHeightForWidth());
        enregistrerButton->setSizePolicy(sizePolicy4);

        buttonHorLay->addWidget(enregistrerButton);

        validerButton = new QPushButton(IOConfig);
        validerButton->setObjectName(QString::fromUtf8("validerButton"));
        sizePolicy4.setHeightForWidth(validerButton->sizePolicy().hasHeightForWidth());
        validerButton->setSizePolicy(sizePolicy4);

        buttonHorLay->addWidget(validerButton);


        genVertLay->addLayout(buttonHorLay);


        gridLayout->addLayout(genVertLay, 0, 0, 1, 1);


        retranslateUi(IOConfig);

        QMetaObject::connectSlotsByName(IOConfig);
    } // setupUi

    void retranslateUi(QWidget *IOConfig)
    {
        IOConfig->setWindowTitle(QApplication::translate("IOConfig", "I/O Configurator", nullptr));
        assiLabel->setText(QApplication::translate("IOConfig", "Assignations", nullptr));
        delAssiButton->setText(QApplication::translate("IOConfig", "x", nullptr));
        sortielabel->setText(QApplication::translate("IOConfig", "Sortie", nullptr));
        addAssiButton->setText(QApplication::translate("IOConfig", "+", nullptr));
        entreelabel->setText(QApplication::translate("IOConfig", "Entr\303\251e", nullptr));
        checkBox->setText(QString());
        label->setText(QApplication::translate("IOConfig", "f(x)", nullptr));
        varLabel->setText(QApplication::translate("IOConfig", "Variables", nullptr));
        addVarButton->setText(QApplication::translate("IOConfig", "+", nullptr));
        valeurLabel->setText(QApplication::translate("IOConfig", "Valeur", nullptr));
        typeLabel->setText(QApplication::translate("IOConfig", "Type", nullptr));
        delVarButton->setText(QApplication::translate("IOConfig", "x", nullptr));
        nomLabel->setText(QApplication::translate("IOConfig", "Nom", nullptr));
        annulerButton->setText(QApplication::translate("IOConfig", "Annuler", nullptr));
        enregistrerButton->setText(QApplication::translate("IOConfig", "Enregistrer", nullptr));
        validerButton->setText(QApplication::translate("IOConfig", "Valider", nullptr));
    } // retranslateUi

};

namespace Ui {
    class IOConfig: public Ui_IOConfig {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_IOCONFIG_H
