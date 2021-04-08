#!/usr/bin/env
from before_strategy import Order, Shipper, ShippingCost


order = Order(Shipper.fedex)
cost_calulator = ShippingCost()
cost = cost_calulator.shipping_cost(order)
assert cost == 3.0

order = Order(Shipper.ups)
cost_calulator = ShippingCost()
cost = cost_calulator.shipping_cost(order)
assert cost == 4.0

order = Order(Shipper.postal)
cost_calulator = ShippingCost()
cost = cost_calulator.shipping_cost(order)
assert cost == 5.0
