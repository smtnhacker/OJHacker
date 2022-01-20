import random

def le11(checker):
    def generator():
        tc = random.randint(1,10)
        gend = [str(tc)]
        inp_tc = [str(tc)]
        for i in range(tc):
            st = []
            q = random.randint(1,20)
            cnt, val = 0, 0
            for j in range(q):
                counter, qc = random.randint(1,4), random.randint(1,2)
                if counter <= 3:
                    st.append('add')
                    val += 1
                else:
                    jt = random.randint(1,200)
                    st.append('for ' + str(jt))
                    cnt += 1
                    val += 1
                if qc == 1 and cnt > 0:
                    st.append('end')
                    cnt -= 1
                    val += 1
            while cnt != 0:
                cnt -= 1
                st.append('end')
                val += 1
            gend.append([str(val)]+st)
            inp_tc.append(str(val)+'\n'+'\n'.join(str(x) for x in st))
        input_tc = '\n'.join(str(x) for x in inp_tc)
        output_tc = str(checker(gend))
        return input_tc, output_tc
        
    return generator