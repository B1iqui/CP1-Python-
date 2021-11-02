digit = 15.84
vat_23 = (23 * digit) / 100

print(f'Amount   : {digit} zl')
def toFixed(vat_23, digits=2):
    return f"{vat_23:.{digits}f}"
print('VAT 23%  : ', toFixed(vat_23),'zl')