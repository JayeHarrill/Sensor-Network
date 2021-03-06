# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-14 02:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('metadata', '0005_auto_20160330_1337'),
    ]

    operations = [
        migrations.CreateModel(
            name='ManualDatapoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datapoint_id', models.IntegerField(default=0)),
                ('timestamp', models.DateTimeField(default=datetime.datetime.now, verbose_name='Timestamp')),
                ('time_to_failure', models.FloatField(default=-1)),
                ('out_pressure', models.FloatField(default=0)),
                ('in_pressure', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Pump',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.IntegerField(default=0)),
                ('pump_name', models.CharField(default='', max_length=200)),
                ('customer_equipment_id', models.IntegerField(default=0)),
                ('pump_serial_number', models.IntegerField(default=0)),
                ('pump_manufacturer', models.CharField(default='', max_length=200)),
                ('pump_model', models.CharField(default='', max_length=200)),
                ('pump_size_x', models.IntegerField(default=0)),
                ('pump_size_y', models.IntegerField(default=0)),
                ('motor_hp', models.FloatField(default=0)),
                ('rpm_rating', models.IntegerField(default=0)),
                ('is_variable_speed', models.BooleanField(default=False)),
                ('motor_voltage_rating', models.FloatField(default=0)),
                ('motor_amperage_rating', models.FloatField(default=0)),
                ('imp_size_inches', models.FloatField(default=0)),
                ('shaft_OR_sleeve_OD', models.FloatField(default=0)),
                ('stuffing_box_OD', models.FloatField(default=0)),
                ('packing_ring_UOM', models.FloatField(default=0)),
                ('lantern_flush_fluid_type', models.CharField(default='', max_length=200)),
                ('packing_X_section_DIM1', models.FloatField(default=0)),
                ('packing_X_section_DIM2', models.FloatField(default=0)),
                ('packing_ring_shape', models.CharField(default='', max_length=200)),
                ('packing_ring_material1', models.CharField(default='', max_length=200)),
                ('packing_ring_material2', models.CharField(default='', max_length=200)),
                ('packing_ring_material3', models.CharField(default='', max_length=200)),
                ('packing_ring_material4', models.CharField(default='', max_length=200)),
                ('packing_ring_material5', models.CharField(default='', max_length=200)),
                ('packing_ring_material6', models.CharField(default='', max_length=200)),
                ('has_lantern_ring', models.BooleanField(default=False)),
                ('lantern_ring_position', models.CharField(default='', max_length=200)),
                ('lantern_flush_volume_flow', models.FloatField(default=0)),
                ('lantern_ring_fluid_pressure', models.FloatField(default=0)),
                ('has_gasket_separator', models.BooleanField(default=False)),
                ('has_throat_brushing', models.BooleanField(default=False)),
                ('lantern_ring_width_inches', models.FloatField(default=0)),
                ('number_of_packing_rings', models.IntegerField(default=0)),
                ('packing_style_used', models.CharField(default='', max_length=200)),
                ('pump_location_gps_latitude', models.FloatField(default=0)),
                ('pump_location_gps_longitude', models.FloatField(default=0)),
                ('pump_location_gps_altitude', models.FloatField(default=0)),
                ('sleeve_material', models.CharField(default='', max_length=200)),
                ('sleeve_install_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='Install Date')),
                ('sleeve_condition_at_start', models.IntegerField(default=0)),
                ('is_from_bulk', models.BooleanField(default=False)),
                ('is_precompressed', models.BooleanField(default=False)),
                ('num_of_studs', models.IntegerField(default=0)),
                ('nominal_flow_in_g_per_min', models.FloatField(default=0)),
                ('nominal_pressure_in_psi', models.FloatField(default=0)),
                ('nominal_pressure_suction_in_psi', models.FloatField(default=0)),
                ('fluid_pumped', models.CharField(default='', max_length=200)),
                ('nominal_solids_percentage', models.FloatField(default=0)),
                ('does_media_change', models.BooleanField(default=False)),
                ('fluid_specific_gravity', models.FloatField(default=0)),
                ('nominal_fluid_temperature_celcius', models.FloatField(default=0)),
                ('gearbox_lube_brand', models.CharField(default='', max_length=200)),
                ('gearbox_lube_iso', models.CharField(default='', max_length=200)),
                ('gearbox_lube_type', models.CharField(default='', max_length=200)),
                ('is_gearbox_lube_synthetic', models.BooleanField(default=False)),
                ('is_installer_trained', models.BooleanField(default=False)),
                ('installer_training_program', models.CharField(default='', max_length=200)),
                ('is_installer_witnessed', models.BooleanField(default=False)),
                ('is_installation_proper', models.BooleanField(default=False)),
                ('maintenance_crew_ID', models.IntegerField(default=0)),
                ('past_maintenance_interval_days', models.IntegerField(default=0)),
                ('target_maintenance_level', models.IntegerField(default=0)),
                ('hourly_cost_of_downtime', models.FloatField(default=0)),
                ('cost_of_water_per_1000_m3', models.FloatField(default=0)),
                ('cost_of_rebuild', models.FloatField(default=0)),
                ('cost_of_sleeve', models.FloatField(default=0)),
                ('cost_of_bearing', models.FloatField(default=0)),
                ('cost_of_labour', models.FloatField(default=0)),
                ('cost_of_lubs', models.FloatField(default=0)),
                ('cost_of_other_rebuild', models.FloatField(default=0)),
                ('cost_of_bearing_seal', models.FloatField(default=0)),
                ('is_critical_application', models.BooleanField(default=False)),
                ('sensor_configuration', models.CharField(default='', max_length=200)),
                ('node_install_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='Node Install Date')),
                ('node_deploy_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='Node Deploy Date')),
                ('bearing_seal_type', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SampleAutomaticDatapoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('node_id', models.IntegerField(default=0)),
                ('datapoint_id', models.IntegerField(default=0)),
                ('load_washer_1_lbs', models.FloatField(default=0)),
                ('load_washer_2_lbs', models.FloatField(default=0)),
                ('gland_follower_position_inches', models.FloatField(default=0)),
                ('force_on_gland_follower_lbs', models.FloatField(default=0)),
                ('equipment_id', models.IntegerField(default=0)),
                ('flush_water_flow_rate', models.FloatField(default=0)),
                ('leakage_rate_cc_per_s', models.FloatField(default=0)),
                ('ambient_temp_C', models.FloatField(default=0)),
                ('shaft_temp_C', models.FloatField(default=0)),
                ('casing_temp_C', models.FloatField(default=0)),
                ('gland_temp_C', models.FloatField(default=0)),
                ('rpm', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_case_id', models.IntegerField(default=0)),
                ('packing_name', models.CharField(default='', max_length=200)),
                ('start_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='Test Start Time')),
                ('packing_inner_diameter_inches', models.FloatField(default=0)),
                ('packing_outer_diameter_inches', models.FloatField(default=0)),
                ('packing_thickness_inches', models.FloatField(default=0)),
                ('surface_finish_rating', models.IntegerField(default=0)),
                ('fluid_type', models.CharField(default='', max_length=200)),
                ('initial_node_voltage', models.FloatField(default=0)),
                ('initial_temperature', models.FloatField(default=0)),
                ('end_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='Test End Time')),
                ('pump', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metadata.Pump')),
            ],
        ),
        migrations.DeleteModel(
            name='TestDatapoint',
        ),
        migrations.RemoveField(
            model_name='node',
            name='arduino_node_id',
        ),
        migrations.RemoveField(
            model_name='node',
            name='bearing_seal_type',
        ),
        migrations.RemoveField(
            model_name='node',
            name='cost_of_bearing',
        ),
        migrations.RemoveField(
            model_name='node',
            name='cost_of_bearing_seal',
        ),
        migrations.RemoveField(
            model_name='node',
            name='cost_of_labour',
        ),
        migrations.RemoveField(
            model_name='node',
            name='cost_of_lubs',
        ),
        migrations.RemoveField(
            model_name='node',
            name='cost_of_other_rebuild',
        ),
        migrations.RemoveField(
            model_name='node',
            name='cost_of_rebuild',
        ),
        migrations.RemoveField(
            model_name='node',
            name='cost_of_sleeve',
        ),
        migrations.RemoveField(
            model_name='node',
            name='cost_of_water_per_1000_m3',
        ),
        migrations.RemoveField(
            model_name='node',
            name='customer_equipment_id',
        ),
        migrations.RemoveField(
            model_name='node',
            name='customer_id',
        ),
        migrations.RemoveField(
            model_name='node',
            name='does_media_change',
        ),
        migrations.RemoveField(
            model_name='node',
            name='fluid_pumped',
        ),
        migrations.RemoveField(
            model_name='node',
            name='fluid_specific_gravity',
        ),
        migrations.RemoveField(
            model_name='node',
            name='gearbox_lube_brand',
        ),
        migrations.RemoveField(
            model_name='node',
            name='gearbox_lube_iso',
        ),
        migrations.RemoveField(
            model_name='node',
            name='gearbox_lube_type',
        ),
        migrations.RemoveField(
            model_name='node',
            name='has_gasket_separator',
        ),
        migrations.RemoveField(
            model_name='node',
            name='has_lantern_ring',
        ),
        migrations.RemoveField(
            model_name='node',
            name='has_throat_brushing',
        ),
        migrations.RemoveField(
            model_name='node',
            name='hourly_cost_of_downtime',
        ),
        migrations.RemoveField(
            model_name='node',
            name='imp_size_inches',
        ),
        migrations.RemoveField(
            model_name='node',
            name='installer_training_program',
        ),
        migrations.RemoveField(
            model_name='node',
            name='is_critical_application',
        ),
        migrations.RemoveField(
            model_name='node',
            name='is_from_bulk',
        ),
        migrations.RemoveField(
            model_name='node',
            name='is_gearbox_lube_synthetic',
        ),
        migrations.RemoveField(
            model_name='node',
            name='is_installation_proper',
        ),
        migrations.RemoveField(
            model_name='node',
            name='is_installer_trained',
        ),
        migrations.RemoveField(
            model_name='node',
            name='is_installer_witnessed',
        ),
        migrations.RemoveField(
            model_name='node',
            name='is_precompressed',
        ),
        migrations.RemoveField(
            model_name='node',
            name='is_variable_speed',
        ),
        migrations.RemoveField(
            model_name='node',
            name='lantern_flush_fluid_type',
        ),
        migrations.RemoveField(
            model_name='node',
            name='lantern_flush_volume_flow',
        ),
        migrations.RemoveField(
            model_name='node',
            name='lantern_ring_fluid_pressure',
        ),
        migrations.RemoveField(
            model_name='node',
            name='lantern_ring_position',
        ),
        migrations.RemoveField(
            model_name='node',
            name='lantern_ring_width_inches',
        ),
        migrations.RemoveField(
            model_name='node',
            name='maintenance_crew_ID',
        ),
        migrations.RemoveField(
            model_name='node',
            name='motor_amperage_rating',
        ),
        migrations.RemoveField(
            model_name='node',
            name='motor_hp',
        ),
        migrations.RemoveField(
            model_name='node',
            name='motor_voltage_rating',
        ),
        migrations.RemoveField(
            model_name='node',
            name='node_deploy_date',
        ),
        migrations.RemoveField(
            model_name='node',
            name='node_install_date',
        ),
        migrations.RemoveField(
            model_name='node',
            name='nominal_flow_in_g_per_min',
        ),
        migrations.RemoveField(
            model_name='node',
            name='nominal_fluid_temperature_celcius',
        ),
        migrations.RemoveField(
            model_name='node',
            name='nominal_pressure_in_psi',
        ),
        migrations.RemoveField(
            model_name='node',
            name='nominal_pressure_suction_in_psi',
        ),
        migrations.RemoveField(
            model_name='node',
            name='nominal_solids_percentage',
        ),
        migrations.RemoveField(
            model_name='node',
            name='num_of_studs',
        ),
        migrations.RemoveField(
            model_name='node',
            name='number_of_packing_rings',
        ),
        migrations.RemoveField(
            model_name='node',
            name='packing_X_section_DIM1',
        ),
        migrations.RemoveField(
            model_name='node',
            name='packing_X_section_DIM2',
        ),
        migrations.RemoveField(
            model_name='node',
            name='packing_ring_UOM',
        ),
        migrations.RemoveField(
            model_name='node',
            name='packing_ring_material1',
        ),
        migrations.RemoveField(
            model_name='node',
            name='packing_ring_material2',
        ),
        migrations.RemoveField(
            model_name='node',
            name='packing_ring_material3',
        ),
        migrations.RemoveField(
            model_name='node',
            name='packing_ring_material4',
        ),
        migrations.RemoveField(
            model_name='node',
            name='packing_ring_material5',
        ),
        migrations.RemoveField(
            model_name='node',
            name='packing_ring_material6',
        ),
        migrations.RemoveField(
            model_name='node',
            name='packing_ring_shape',
        ),
        migrations.RemoveField(
            model_name='node',
            name='packing_style_used',
        ),
        migrations.RemoveField(
            model_name='node',
            name='past_maintenance_interval_days',
        ),
        migrations.RemoveField(
            model_name='node',
            name='pump_location_gps_altitude',
        ),
        migrations.RemoveField(
            model_name='node',
            name='pump_location_gps_latitude',
        ),
        migrations.RemoveField(
            model_name='node',
            name='pump_location_gps_longitude',
        ),
        migrations.RemoveField(
            model_name='node',
            name='pump_manufacturer',
        ),
        migrations.RemoveField(
            model_name='node',
            name='pump_model',
        ),
        migrations.RemoveField(
            model_name='node',
            name='pump_serial_number',
        ),
        migrations.RemoveField(
            model_name='node',
            name='pump_size_x',
        ),
        migrations.RemoveField(
            model_name='node',
            name='pump_size_y',
        ),
        migrations.RemoveField(
            model_name='node',
            name='raspi_node_id',
        ),
        migrations.RemoveField(
            model_name='node',
            name='rpm_rating',
        ),
        migrations.RemoveField(
            model_name='node',
            name='sensor_configuration',
        ),
        migrations.RemoveField(
            model_name='node',
            name='shaft_OR_sleeve_OD',
        ),
        migrations.RemoveField(
            model_name='node',
            name='sleeve_condition_at_start',
        ),
        migrations.RemoveField(
            model_name='node',
            name='sleeve_install_date',
        ),
        migrations.RemoveField(
            model_name='node',
            name='sleeve_material',
        ),
        migrations.RemoveField(
            model_name='node',
            name='stuffing_box_OD',
        ),
        migrations.RemoveField(
            model_name='node',
            name='target_maintenance_level',
        ),
        migrations.AddField(
            model_name='node',
            name='associated_raspi_node_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='node',
            name='current_equipment_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='node',
            name='node_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='node',
            name='node_firmware_version',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='node',
            name='node_hardware_version',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='node',
            name='node_name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='nodeowner',
            name='node_owner_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='nodeowner',
            name='owner_name',
            field=models.CharField(default='NA', max_length=200),
        ),
        migrations.AddField(
            model_name='pump',
            name='nodeowner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metadata.Nodeowner'),
        ),
    ]
