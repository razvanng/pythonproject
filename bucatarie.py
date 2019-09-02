from pizza import Pizza


pizza1=Pizza('Subtire','Mare',['x','y','z'],'Capriciosa')



pizza1.addtoping(['sunca','carnati','porumb'])
pizza1.set_price()
pizza1.description()
pizza1.removetopings(['carnati','sunca','alune'])
pizza1.getpizzadescription()


pizza1.removealltoppings()
pizza1.set_price()
pizza1.description()


pizza2=Pizza('Subtire','Mare',['carnati','porumb'])
pizza2.removealltoppings()
pizza2.getpizzadescription()



