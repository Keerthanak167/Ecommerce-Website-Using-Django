# Generated by Django 5.0.3 on 2025-07-17 14:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_remove_orderitem_price_alter_order_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='store.order'),
        ),
    ]
