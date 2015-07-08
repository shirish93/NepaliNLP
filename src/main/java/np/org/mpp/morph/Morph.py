class Morph:
  __init__(self):
    self.parsetwo = 0;

    self.sdes, self.smorph, self.pdes, self.respuff, self.pmorph = [ ['' for each in range(10)] for each in range(5)]
    
    self.subsmorph, self.smorph_rulenum = [[0 for each in range(10)] for each in range(2)]
    
    self.suffix, self.prefix, self.suffix_index, self.prefix_index, self.suffix_rule,
      self.prefix_rule, self.root, self.tmpgen, self.isSuffixRoot, self.suffix_root,
      self.root_pos = ["" for each in range(11)]
    
    self.dspresent= False

    self.rulenumber, self.smorph_number, self.pmorph_number, self.dub_len, self.spnt, self.i,
      self.k, self.go, self.repcom, self.rec = [0 for each in range(10)]
     
    self.present = "no"

    self.suf_sub_rule, self.suffix_del , self.suffix_exist , self.suffix_look_posi, 
    self.suffix_look_char , self.suffix_desc, self.suffix_ins , self.suffix_ins_posi, self.suffix_morph,
    self.suffix_type, self.suffix_ign, self.dub_suffix, self.dub_suffix_morph,  self.dub_suffix_desc,
    self.pre_sub_rule, self.prefix_del, self.prefix_desc, self.prefix_ins, self.prefix_morph,
    prefix_type = [dict() for each in range(20)]

    with open("tokenizerdata/newfile2", "r") as f: 
      q = [' '.join(each for each in f)].split('\n')
    for each in q:
      tmp = each
      if '|' in tmp:
        tmp = q[qcount];
        tok = tmp.split('|')
        ht_root[tok[0]] = tok[0]
        ht_root_pos[tok[0]] = tok[1]
        if len(tok)>2:
          suffix_exist(tok[0]) = tok[2]
        else:
          suffix_exist(tok[0]) = 'null'
      else:
        ht_root[tmp]= tmp
        ht_root_pos[tmp]= "null"
        suffix_exist[tmp]= "null"

    with open("tokenizerdata/alt_root.txt", 'r') as f:
      st = [each for each in f]
    for each in st:
      part_st = each.split(" ")
      alt_root[part_st[0]] = part_st[1]
      suffix_exist[part_st[0]] = "null"

    with open("tokenizerdata/suffix.txt", 'r') as f:
      st = [each for each in f]
    for each in st:
      part_st = each.split('|')
      tmp1 = part_st[0]
      ht_suffix[tmp1]= tmp1
      if len(part_st)>1:
        suffix_ht[tmp1] = part_st[1]

    with open("tokenizerdata/suffix_rule.txt", 'r') as f:
      st = [each for each in f]
    for q, each in enumerate(st):
      nextq = q
      part_st = each.split(" ")
      val = int(str(part_st[0]))
      suffix_type[val]= part_st[1]
      suf_sub_rule[val] = part_st[2]
      suffix_morph[val] = part_st[3]
      suffix_desc[val] = part_st[4]
      suffix_ign[val] = part_st[5]
      s = int(str(sub_sub_rule[val]))
      if suffix_type[val] == "SFX":
        for b in range(0, s):
          nextq +=1
          srule = st[nextq].split(" ")
          suffix_del[val+str(b)]= srule[0]
          suffix_ins[val+str(b)]= srule[1]
      elif suffix_type[val] == "SFXX":
          for b in range(0, s):
            srule = st[nextq].split(' ')
            suffix_del[val+str(b)]= srule[0]
            suffix_look_posi[val+str(b)] = srule[1]
            suffix_look_char[val+str(b)] = srule[2]
            suffix_ins_posi[val+str(b)] = srule[3]
            suffix_ins [val+str(b)]  = srule[4]

    with open("tokenizerdata/prefix.txt", 'r') as f:
      s = [each for each in f]
    for each in st:
      part_st = each.split('|')
      tmp1 = part_st[0]
      ht_prefix[tmp1] = tmp1
      lenpart_st = len(part_st)
			if lenpart_st>1:
        prefix_tm[tmp1] = part_st[1]

    with open("tokenizerdata/prefix_rule.txt", 'r') as f:
      st = [each for each in f]
    for q, each in enumerate(st):
      part_st = each.split(" ")
      nextst = q
      val = str(part_st[0])
      value = int(val)
      prefix_type[val] = part_st[1]
      pre_sub_rule[val] = part_st[2]
      prefix_morph [val] = part_st[3]
      prefix_desc[val] = part_st[4]
      s = int(str(pre_sub_rule[val]))
      if prefix_type[val]=="PFX":
        for b in range(0, s):
          nextst +=1
          srule = st[nextst].split(' ')
          prefix_del[val+str(b)] = srule[0]
          prefix_ins[val+str(b)] = srule[1]

    with open("tokenizerdata/dub_suffix.txt") as f:
      a = [each for each in f]
    for each in a:
      b = each.split(' ')
      dub_suffix[b[0]]=b[0]
      dub_suffix_morph[b[0]] = b[1]
      dub_suffix_desc[b[0]] = b[2]
	
	# is it an alternate root?
	def isAltRoot( tmp):
		if (tmp in alt_root):
			setRootPos( str(ht_root_pos[alt_root[tmp]]))
			return true
		else:
			return false

	# get the alternate root
	def getAltRoot(tmp):
		return str(alt_root[tmp])

	def getSuffixExist(e):
		return str(suffix_exist[e])
	
	def getSDes():
		return sdes

	def getSDesat(i):
		return sdes[i]
	
  def getPDes():
		return pdes
	
	def getSMorph():
		return smorph

	def getSMorphat( i):
		return smorph[i]
	
	def getPMorph():
		return pmorph

	def getSMorph_number():
		return smorph_number

	def getPMorph_number():
		return pmorph_number

	def getRoot():
		return root

	def getRuleNumber():
		return rulenumber

	def getSuffix_rule():
		return suffix_rule

	def isRoot(stri):
		if stri == ht_root[stri]:
			root_pos = str(ht_root_pos[stri])
			return true
		return false

	def getRootPos():
		return root_pos
	
  def setRootPos(pos):
		root_pos = pos
	
	def setSDes(d, i):
		sdes[i] = d
	
	def setSMorph(mor,  i):
		print(mor)
		smorph[i] = mor

	def setSuffixRoot(m):
		isSuffixRoot = m
	
  def getSuffixRoot():
		return isSuffixRoot

	def setSMorph_rulenum( i,  j):
		smorph_rulenum[i] = j

	def getSMorph_rulenum( i):
		return smorph_rulenum[i]

	def setSubSMorph( subnum, i):
		subsmorph[i] = subnum

	def getSubSMorph( i):
		return subsmorph[i]

	def setSecParse( i):
		parsetwo = i

	def setSMorph_number( number):
		this.smorph_number = number

	def setPDes(d, i):
		pdes[i] = d

	def setPMorph(mor, i):
		pmorph[i] = mor

	def setPMorph_number(number):
		this.pmorph_number = number

	def void setRoot(stri):
		root = stri

	def setRuleNumber(i):
		rulenumber = i

	def setSuffix_rule(suffix_rule):
		this.suffix_rule = suffix_rule

	#
	# mn=morph number. This generate the word with the specific suffix
	# rn=rulenumber
	#
	def generateWord(r1, mn):
    q = r1
    t = str(smorph_rulenum[mn])
    a = str(suffix_del[t+str(subsmorph[mn])])
		dot = ''
		l = len(q)
		b = int(str(suf_sub_rule[t]))
		if (suffix_type[t] =="SFX"):
      for s in range(s, b):
        if subsmorph[mn] == s:
          dot = suffix_ins[t+str(s)]
          if dot!= '.':
            length = len(dot)
            q = q[:l-length]+q[l:]
            q = q+a
            tmpgen = str(q)
            break
          else:
            q = q+a
      tmpgen = str(q)
    elif suffix_type[t] == "SFXX":
      tmpgen = str(q)

    return tmpgen


  def stripSuffix(word):
    w = word
    rulenumber, tmp1, tmp2 = '', '', ''
    l_tmp=0
    b = int(str(suf_sub_rule[str(getRuleNumber())]))
    rulenumber = str(getRuleNumber())
    setSMorph(str(suffix_morpoh[rulenumber]), getSMorph_number())
    setSMorph_rulenum(getSmorph_number(), int(rulenumber))
    setSDes(str(suffix_desc[rulenumber]), getSMorph_number())
    if suffix_type[rulenumber] == "SFX":
      for s in range(0, b):
        lengthw = len(w)
        if word.endsWith(str(suffix_del[rulenumber+str(s)])):
          setSubSMorph(s, getSMorph_number())
          tmp1 = str(suffix_del[rulenumber+str(s)])
          tmp2 = str(suffix_ins[rulenumber+str(s)])
          l_tmp = len(tmp1)
          w = w[:lengthw]+w[l_tmp:]
          if tmp2 != '.':
            w=w.append(tmp2)
          break
      setRoot(str(w))

    if suffix_type[rulenumber]=="SFXX":
      for s in range(0, b):
        s_l_p = str(suffix_look_posi[rulenumber+str(s)])
        s_l_c = str(suffix_look_char[rulenumber+str(s)])
        look_posi = s_l_p.split("|")
        look_char = s_l_c.split("|")
        l_p = ['' for each in range(2)]
        l_c = ['' for each in range(2)]
        z=0, q=0
        
        for i, token in enumerate(look_posi):
          l_p[q] = str(token)
          l_c[q] = str(look_char[i])
          q+=1
        
        for j in range(0, q):
          ini, fin = 0
          l = len(l_c[j])
          if l_p[j] != ">":
            ini = int(l_p[j])
            fin = int(l_p[j])+l
          else:
            ini = len(w)-l+1
            fin = len(w)-1
          if w[ini:fin] == l_c[j]:
            z+=1

        if (q==z):
          lengthw = len(w)
          delete_string = str(suffix_del[rulenumber+str(s)])
          if delete_string != '.':
            w = w[:lengthw - len(delete_string)]+w[lengthw:]
          s_i_p = str(suffix_ins_posi[rulenumber+str(s))
          s_i_c = str(suffix_ins[rulenumber+str(s)])
          ins_posi = s_i_p.split("|")
          ins_char = s_i_c.split("|")
          s_i_p_a = ['' for each in range(2)]
          s_i_c_a = ['' for each in range(2)]
          p = 0
          for ind, each in enumerate(ins_posi):
            s_i_p_a[p] = ins_posi[ind]
            s_i_c_a[p] = ins_char[ind]
            p++
          for i in range(0, p):
            if s_i_p_a[i] != '.':
              if s_i_p_a == '>':
                w+=s_i_c_a[i]
              else:
                inPos = int(s_i_p_a[i])
                w[inPos] = s_i_c_a[i]
          break
    setRoot(str(w))

	def isASuffix(word):
		w = word
		w+="\u094d"
		a = w
		c = 9998
		i = getSMorph_number()
		setSMorph_number(i)
    setSMorph(str(suffix_morph[str(c)]), i)
    setSDes(str(suffix_desc[str(c)]), i)
		setRoot(a)

	#check for wheather the rule has to be skipped for smaller suffixes to be
	#handled.
	def isRepeat(rn):
		return str(suffix_ign[rn])=="Y"

	def suffixPresent(stri, o):
		present = "no"
    for rn in range(1, len(stri)):
      tmp = stri[-rn]
      if tmp == ht_suffix['tmp']:
        if parsetwo ==1:
          if isRepeat(str(suffix_ht[tmp])):
            for j in range(0, rec+1):
              if repsuff[j]==tmp:
                present = "yes"
            if present == "no":
              setRuleNumber(int(str(suffix_ht[tmp])))
              return True
          else:
            setRuleNumber(int(str(suffix_ht[tmp])))
            return True
        else:
          rec = o
          setRuleNumber(int(str(suffix_ht[tmp])))
          repsuff[rec]=tmp
          return True
    return False

	def prefixPresent(stri):
    for rn in range(0, len(stri)):
      tmp = stri[0, rn+1]
      if tmp==ht_prefix[tmp]:
        setRuleNumber(int(str(prefix_tm[tmp])))
        return True
    return False

	def stripPrefix( w ):
		w = new StringBuffer(word)
    b = int(pre_sub_rule[str(getRuleNumber)])
    ruleNumber = str(getRuleNumber)
    
    setPMorph (str(prefix_morph[rulenumber]), getPMorph_number())
    setPDes (str(prefix_desc[rulenumber]), getPMorph_number())
		setPMorph(prefix_morph.get(rulenumber).toString(), getPMorph_number());
		setPDes(prefix_desc.get(rulenumber).toString(), getPMorph_number());

    if prefix_type[rulenumber]=="PFX":
      for s in range(0, b):
        if word.startswith(str(prefix_del[rulenumber+str(s)])):
          tmp = prefix_del[str(rulenumber + str(s))]
          w = w[len(tmp):]#possible error here. len(tmp) or len(tmp)+1??? how does str.repl work in java?
          break
    
    setRoot(str(w))

  def handleDuplicateWord(s):
    dub_len = len(s)
    recur = dub_len/2
    i=0
    while (i<recur):
      if s.substring(0, i+1) == s.substring(i+1, (i+1)*2):
        if (i+1)*2 != len(s):
          tmp_suffix = s.substring((i+1)*2, len(s)):
          if tmp_suffix == dub_suffix[tmp_sufix]:
            setRoot(s.substring(0, (i+1)*2))
            setRootPos("duplicate")
            setPMorph_number(0)
            setSMorph_number(1)
            setSMorph(str(dub_suffix_morph[tmp_suffix]), 1)
            setSDes(str(dub_suffix_desc[tmp_suffix]), 1)
        else:
          setPMorph_number(0)
          setSMorph_number(0)
          setRoot(s)
          setRootPos("duplicate")
      i+=1

	def handleCompoundWord(rl):
    i,go,repcom =0
    setPMorph_number(0);
    setSMorph_number(0);
    lengthq = len(rl)
    while go==0:
      repcom+=1
      go+=1
      for l in range(0, l):
        tmp = rl[-l]
        if tmp == ht_suffix[tmp]:
          if repcom==1:
            if isRepeat(str(suffix_ht[tmp])):
              go = 0
              break
          i+=1
          setSMorph_number(i)
          setRuleNumber(int(str(suffix_ht[tmp])))
          b = int(str(suf_sub_rule[str(getRuleNumber())]))
          ruleNumber = str(getRuleNumber)
          setSMorph(str(suffix_morph[rulenumber]), getSMorph_number())
          setSMorph_rulenum(getSMorph_number(), int(rulenumber))
          setSDes(str(suffix_desc[rulenumber]), getSmorph_number())
        
      

 {
		while (go == 0) {
			for (int l = 0; l < lengthw; l++) {
				if (tmp.equals(ht_suffix.get(tmp))) {

###START TRANSLATING FROM BELOW:

					if (suffix_type.get(rulenumber).equals("SFX")) {
						for (int p = 0; p < b; p++) {

							if (tmp.equals(suffix_del.get(
									rulenumber + String.valueOf(p)).toString())) {
								// record the subrule number generation
								setSubSMorph(p, getSMorph_number());

								tmp1 = suffix_del.get(
										rulenumber + String.valueOf(p))
										.toString();
								tmp2 = suffix_ins.get(
										rulenumber + String.valueOf(p))
										.toString();

								l_tmp = tmp1.length();

								r1.replace(lengthw - l_tmp, lengthw, "");

								if (!tmp2.equals(".")) {
									r1.append(tmp2);
								}
								break;
							}
						}

						// setRoot(r1.toString());
					}
					l = -1;
					lengthw = r1.length();
					// r1=r1.replace(0,r1.length(),"");
					// r1.append(getRoot()) ;

				} else if (tmp.equals(ht_root.get(tmp))
						&& !getSuffixExist(tmp).equals("N")) {
					i++;
					setSMorph_number(i);
					setSMorph(tmp, i);
					setSDes(ht_root_pos.get(tmp).toString(), i);
					r1 = r1.replace(r1.length() - tmp.length(), r1.length(), "");
					lengthw = r1.length();
					l = -1;
				} else /*
						 * if(tmp.substring(0,tmp.length()-1).equals(ht_root.get(
						 * tmp.substring(0,tmp.length()-1)))){
						 * 
						 * r1=r1.replace(r1.length()-tmp.length(),r1.length(),"")
						 * ; lengthw=r1.length(); l=-1; }else
						 */if (tmp.equals(ht_root.get(tmp + "\u093e"))) {
					i++;
					setSMorph_number(i);
					setSMorph(tmp + "\u093e", i);
					setSDes(ht_root_pos.get(tmp + "\u093e").toString(), i);
					r1 = r1.replace(r1.length() - tmp.length(), r1.length(), "");
					lengthw = r1.length();
					l = -1;
				}/*
				 * else if(prefixPresent(tmp)){ k++; setPMorph_number(k);
				 * stripPrefix(tmp); r1=r1.replace(0,r1.length(),"");
				 * r1.append(getRoot()) ; }
				 */
			}
		}
		tmp = r1.toString();
		if (!tmp.isEmpty()) {
			if (tmp.endsWith("\u094d")
					&& isRoot(tmp.substring(0, tmp.length() - 1))) {
				setRoot(tmp.substring(0, tmp.length() - 1));
			} else {
				setRoot("unrecognized");
			}
		} else {
			setRoot(getSMorphat(i));
			setRootPos(getSDesat(i));
			setSMorph_number(i - 1);
		}
	}
	/*
	 * public static void main(String args[]){ Morph m = new Morph(); }
	 */
}
