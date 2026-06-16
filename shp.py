# ..................is ka matlab module import hua phr
# function ko full path se caal kiya..................

import ecommerce.shipping
ecommerce.shipping.calc_shipping()


#............ is ka matlab hai k sirf specific function import hua
# ab ap direct use kr sakty hu issay...................

from ecommerce.shipping import calc_shipping
calc_shipping()

