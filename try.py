fout = open('write.txt', 'w')

fout.write('D) {0} \n'.format(defdict['Pimg']))
fout.write('E) {0} \n'.format(defdict['PSFf']))
fout.write('F) {0} \n'.format(defdict['badmask']))
fout.write('G) {0} \n'.format(defdict['constr']))
fout.write('H) {0} \n'.format(defdict['region']))
fout.write('I) {0} \n'.format(defdict['convbox']))
fout.write('J) {0} \n'.format(defdict['ZP']))
fout.write('K) {0} \n'.format(defdict['scale']))
fout.write('O) {0} \n'.format(defdict['dispt']))
fout.write('P) {0} \n'.format(defdict['opt']))

fout.close()
