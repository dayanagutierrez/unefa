version="1.0"coding="utf-8"?>
<openerp>
    <data>
        <record model="ir.ui.view" id="view_modelo_autos_form">
            <field name="name">modelo_autos_form</field>
            <field name="model">modelo.autos</field>
            <field name="type">form</field>
            <field name="arch" type="xml">
                <form string="autos">
                    <group>
                        <field name="propietario"/>
                        <field name="cedula_id"/>
                        <field name="color"/>
                        <field name="modelo_id"/>
                        <field name="fecha_entrada"/>
                        <field name="hora_entrada"/>
                        <field name="fecha_salida"/>
                        <field name="hora_salida"/>
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
                <tree string="autos">
                    <group>
                        <field name="propietario"/>
                        <field name="cedula_id"/>
                        <field name="color"/>
                        <field name="modelo_id"/>
                        <field name="fecha_entrada"/>
                        <field name="hora_entrada"/>
                        <field name="fecha_salida"/>
                        <field name="hora_salida"/>
                        <field name="active"/>
                    </group>
                </tree>
            </field>
        </record>


        <record model="ir.actions.act_window" id="action_modelo_autos">
            <field name="name">modelo autos</field>
            <field name="res_model">modelo.autos</field>
            <field name="view_type">form</field>
            <field name="view_mode">tree,form</field>
        </record>

        <menuitem name="modelo" id="menu_modelo" sequence="10"/>
        <menuitem name="Inicio" id="menu_inicio" parent="menu_modelo" sequence="10"/>
        <menuitem name="autos" id="menu_autos" action="action_modelo_autos" parent="menu_modelo" sequence="10"/>
    </data>
</openerp>
