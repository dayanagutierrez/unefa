<?xml version="1.0" encoding="utf-8"?>
<openerp>
    <data>
        <record model="ir.ui.view" id="view_modelo_autos_form">
            <field name="name">modelo_autos_form</field>
            <field name="model">modelo.autos</field>
            <field name="type">form</field>
            <field name="arch" type="xml">
                <form string="modelo">
                    <group>
                        <field name="modelo"/>
                        <field name="active"/>
                    </group>
                </form>
            </field>
        </record>

        <record model="ir.ui.view" id="view_modelo_autos_tree">
            <field name="name">modelo_autos_tree</field>
            <field name="model">modelo.autos</field>
            <field name="type">tree</field>
            <field name="arch" type="xml">
                <tree string="modelo">
                    <group>
                        <field name="modelo"/>
                        <field name="active"/>
                    </group>
                </tree>
            </field>
        </record>


        <record model="ir.actions.act_window" id="action_modelo_autos">
            <field name="name">autos modelo</field>
            <field name="res_model">autos.modelo</field>
            <field name="view_type">form</field>
            <field name="view_mode">tree,form</field>
        </record>

        <menuitem name="Unefa" id="menu_modelo" sequence="10"/>
        <menuitem name="Inicio" id="menu_inicio" parent="menu_modelo" sequence="10"/>
        <menuitem name="modelo" id="menu_modelo" action="action_autos_modelo" parent="menu_modelo" sequence="10"/>
    </data>
</openerp>
