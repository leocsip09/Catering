use catering;

drop procedure if exists Agregar_Ingrediente;
delimiter //
create procedure Agregar_Ingrediente(in nom_ingr varchar(40), in cant_req int, in id_men int, in id_prov int)
begin
	if id_prov in (select i.id_proveedor from inventario i inner join proveedor p on i.id_proveedor = p.id_proveedor where i.nombre_producto = nom_ingr) then
        insert into ingredientes (precio_unidad, unidad_medida, cantidad_requerida, nombre_ingrediente, id_menu, id_proveedor) 
			values
				((select i.precio_unidad + (i.precio_unidad * 18/100) from inventario i where nom_ingr = i.nombre_producto and id_prov = i.id_proveedor),
                (select i.unidad_medida from inventario i where nom_ingr = i.nombre_producto and id_prov = i.id_proveedor),
                cant_req,
                nom_ingr,
                id_men,
                id_prov);
	end if;
end;
//
delimiter ;
