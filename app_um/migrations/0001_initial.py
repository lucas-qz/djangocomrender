# Generated by Django 5.0.7 on 2024-07-15 16:31

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="D_Caracteres",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("N_Char", models.CharField(max_length=4)),
                ("N_Text", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="D_Datas_E_Horas",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("N_Date", models.DateField()),
                ("N_Time", models.TimeField()),
                ("N_DateTime", models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name="D_Numeros_Com_Virgula",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("N_Decimal", models.DecimalField(decimal_places=2, max_digits=3)),
                ("N_Float", models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name="D_Numeros_Inteiros",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("N_BigInt", models.BigIntegerField()),
                ("N_Int", models.IntegerField()),
                ("N_SmallInt", models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="D_Numeros_Inteiros_Positivos",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("N_BigInt", models.PositiveBigIntegerField()),
                ("N_Int", models.PositiveIntegerField()),
                ("N_SmallInt", models.PositiveSmallIntegerField()),
            ],
        ),
    ]
