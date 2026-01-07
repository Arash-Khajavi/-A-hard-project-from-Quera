def saeedeh_pyramid(s: str):
    line_length = 0
    l=[]
    k=[]
    for i in range(0,len(s)):
         line_length+=1
         k.append(line_length)
    for i in s:
        l.append(i)
    kj=[]
    for ty in k:
        # print(ty)
        if ty == 1:
            # print(ty,l[ty-1])
            kj.append(l[ty-1])
            l.remove(l[ty-1])
        try:
            if ty > 1:
                # print( l[ty-2:ty+ty-2])
                # print(ty,"".join(l[ty-ty:ty+ty-ty]))
                kj.append("".join(l[ty-ty:ty+ty-ty]))
                for u in l[ty-ty:ty+ty-ty]:
                 l.remove(u)
                # print(l)
                # print(kj)
        except:
            pass
    # print(kj)
    for u in range(len(kj)):
        if u % 2 != 0:
            kj.insert(u,str("\n"))
    kj.reverse()
    # print(kj)
    j=[]
    # print("".join(kj))
    # print(kj)
    j.append("".join(kj))
    # print(j)
    for mn in k:
        for un in kj:
            if un == '':
                kj.remove(un)
                # print(kj)
                kj.remove(kj[0])
                # print(kj)
    # print(kj)
    kj.reverse()
    # print(kj)

    for yu in range(kj.count("\n")):
        kj.remove("\n")
    # print(kj)
    for uh in kj:
        k.append(uh)
    # print(k)
    for hgj in range(len(kj)):
        for mn in k[:len(kj)]:
            index=k.index(mn)
            f=index+len(s)
            try:
                if len(k[f]) != mn:
                    # print(k[f])
                    cal=mn-len(k[f])
                    p=cal
                    for uyt in range(cal):
                        nb=kj.index(k[f])
                        k[f]+="#"
                        # print(k[f])
                        kj[nb]=k[f]
                        # print(kj)

                        for i in range(len(kj)+len(kj)-1):
                            if i % 2 != 0:
                                # print(i)
                                kj.insert(i,"\n")
                                # kj.reverse()
                                # print(kj)
                            break

                    break
            except:
                pass
    kj.reverse()
    # print("".join(kj))
    for i in range(len(kj) + len(kj) - 1):
        if i % 2 != 0:
            # print(i)
            kj.insert(i, '\n')
            # kj.reverse()
            # print(kj)

    # print(kj)
    print("".join(kj))

    # m=str("/")
    # print(m)
    # for i in range(len(kj) + len(kj) - 1):
    #     if i % 2 != 0:
    #         print(i)
    #         kj.insert(i, "\n")
    #
    # print("".join(kj))
saeedeh_pyramid('abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')


















def saeedeh_pyramid(s):
    global y
    l=[]
    for i in range(1,len(s)+1):
        line_length = 0
        line_length+=i
        # print(line_length)
        l.append(line_length)
    l.reverse()
    # print(l)
    k=[]
    kj1=[]
    for hg in s:
        k.append(hg)
    k.reverse()
    # print(k)
    for u in k:
     kj1.append(u)
    j = []
    for u in range(len(l)):
        # print(k[u])
        v=k[:u]

        # print(v)
        for yt in v:
            # print(yt)
            k.remove(yt)
        j.append(v)
    # print(j)
    kj=[]
    kh5=[]
    for hjt in range(len(j)):
        if [] in j:
            j.remove([])
            # print(j)
            kj.append(j)
    # print(kj[-1])
    number_of_lines=len(kj[-1])
    # print(number_of_lines)
    # print(kj1)
    kh = []
    bv=""
    for tyu in range(1,number_of_lines+1):
        if tyu == 1:
         # print(kj1[-1])
         kh.append(kj1[-1])
         kj1.remove(kj1[-1])

        if tyu > 1:
            pr=kj1[-tyu:]
            # print("".join(pr)[::-1])
            kh.append("".join(pr)[::-1])
            kh5.append("".join(pr)[::-1])
            for h in pr:
             kj1.remove(h)
    f=l.index(number_of_lines)
    # print(kh)
    for tyu in l[f:][::-1]:
        kh.append(tyu)
    # print(kh)
    # print(kh5)
    for i in kh5:
        g=kh.index(i)
        if kh[g+4] != len(kh[g]):
            bn1=kh[g+number_of_lines]-len(kh[g])
            for gh1 in range(bn1):
              kh[g]+="#"
              # print(kh[g])
              kh.insert(g,kh[g])
    jt=[]
    # print(len(kh[:number_of_lines]))
    jt.append(kh[:number_of_lines])
    for y in jt:
        # print(y)
        pass
    gf=[]
    for gh in y:
        gf.append(gh)
    # print(gf)
    for ytu in range(len(gf)+len(gf)-1):
            if ytu % 2 !=0:
                gf.insert(ytu,"\n")
    gf.reverse()
    print("".join(gf))
saeedeh_pyramid("abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")
