# Rules of Game:

- Given 4 numbers A B C D
- ABCD can be 0-9
- Operators: +, -, *, /, ^
- Number Transformers: !, sqrt, -()
- Parenthesis

# Scope of App:

- Solution Points
- Database of Solutions

- Rearrange Numbers
- Multi Digit Numbers I.E 2019: 20 - 1 - 9
- More than 4 numbers
- Visualiser
- Gamemode:
    - Solve yourself
    - Numbers Given to you
    - Ur own numbers
- Social Online Comp aspect for daily commuters

# Code Design:

- Optimise
- Case Exclusion by size
- Graph Theory to Optimise

### Examples

5531 → sqrt(5*5) + 3! -1, 5 *(-(5-3!)+1)

3577 → 3! / (-(5-7)) + 7

1472

0007

9444

3222

6561 → sqrt(100) → sqrt((6!-5!)/6*1)

1611

### **Basic Operators**

$`A~O_0~B~O_1~C~O_2~D = 10`$

$`O_0,~O_1,~O_2`$   **:**   **+, -, *, /, ^** 

**Possible Combinations:** $`5^3 = 125`$

### **Factorial and Sqrt**

$`(T_AA)~O_0~(T_BB)~O_1~(T_CC)~O_2~(T_DD) = 10`$

$`T_A,~T_B,~T_C,~T_D:~()!,~\sqrt()`$

**Possible Combinations:** $`5^3 *3^4=10125`$ 

### **Vector Direction**

$`(\pm A)~O_0~(\pm B)~O_1~(\pm C)~O_2~(\pm D) = 10`$

**Possible Combinations:** $`5^3*2^4=2000`$ 

### **FSV Combo**

$`(\pm T_AA)~O_0~(\pm T_BB)~O_1~(\pm T_CC)~O_2~(\pm T_DD) = 10`$

**Possible Combinations:** $`5^3*5^4*2^4=1~250~000`$ 

### **Brackets**

*Case 0:  ABCD*

$`(\pm T_AA)~O_0~(\pm T_BB)~O_1~(\pm T_CC)~O_2~(\pm T_DD) = 10`$

**Possible Combinations:** $`5^3*5^4*2^4=1~250~000`$ 

*Case 1:  (AB)(CD)*

$`\bigl ((\pm T_AA)~O_0~(\pm T_BB)\bigl )~O_1~\bigl ((\pm T_CC)~O_2~(\pm T_DD)\bigl ) = 10`$

**Possible Combinations:** $`5^3*5^4*2^4=1~250~000`$ 

*Case 2:  ((AB)C)D*

$`\Bigl(\bigl((\pm T_AA)~O_0~(\pm T_BB)\bigl)~O_1~(\pm T_CC)\Bigl)~O_2~(\pm T_DD) = 10`$

**Possible Combinations:** $`5^3*5^4*2^4=1~250~000`$ 

*Case 3: (A(BC))D*

$`\Bigl((\pm T_AA)~O_0~\bigl((\pm T_BB)~O_1~(\pm T_CC)\bigl)\Bigl)~O_2~(\pm T_DD) = 10`$

**Possible Combinations:** $`5^3*5^4*2^4=1~250~000`$ 

*Case 4:  A((BC)D)*

$`(\pm T_AA)~O_0~\Bigl(\bigl((\pm T_BB)~O_1~(\pm T_CC)\bigl)~O_2~(\pm T_DD)\Bigl) = 10`$

**Possible Combinations:** $`5^3*5^4*2^4=1~250~000`$ 

*Case 5:  A(B(CD))*

$`(\pm T_AA)~O_0~\Bigl((\pm T_BB)~O_1~\bigl((\pm T_CC)~O_2~(\pm T_DD)\bigl)\Bigl) = 10`$

**Possible Combinations:** $`5^3*5^4*2^4=1~250~000`$ 

**Total Combinations: $`6*(5^3*5^4*2^4)= 7~500~000`$**

### **AB/ABC/ABCD FSV**

*Case 0:  ABCD*

$`T_{ABCD=100}\Bigl((\pm T_AA)~O_0~(\pm T_BB)~O_1~(\pm T_CC)~O_2~(\pm T_DD)\Bigl) = 10`$

**Possible Combinations:** $`5^3*5^4*2^4*2=2~500~000`$ 

*Case 1:  (AB)(CD)*

$`T_{ABCD=100}\Bigl(\pm T_{AB}\bigl ((\pm T_AA)~O_0~(\pm T_BB)\bigl )~O_1~\pm T_{CD}\bigl ((\pm T_CC)~O_2~(\pm T_DD)\bigl)\Bigl) = 10`$

**Possible Combinations:** $`5^3*5^6*2^6*2=250~000~000`$  

*Case 2:  ((AB)C)D*

$`T_{ABCD=100}\biggl(\pm T_{ABC}\Bigl(\pm T_{AB}\bigl((\pm T_AA)~O_0~(\pm T_BB)\bigl)~O_1~(\pm T_CC)\Bigl)~O_2~(\pm T_DD)\biggl) = 10`$

**Possible Combinations:** $`5^3*5^6*2^6*2=250~000~000`$  

*Case 3: (A(BC))D*

$`T_{ABCD=100}\biggl(\pm T_{ABC}\Bigl((\pm T_AA)~O_0~\pm T_{BC}\bigl((\pm T_BB)~O_1~(\pm T_CC)\bigl)\Bigl)~O_2~(\pm T_DD)\biggl) = 10`$

**Possible Combinations:** $`5^3*5^6*2^6*2=250~000~000`$  

*Case 4:  A((BC)D)*

$`T_{ABCD=100}\biggl((\pm T_AA)~O_0~\pm T_{BCD}\Bigl(\pm T_{BC}\bigl((\pm T_BB)~O_1~(\pm T_CC)\bigl)~O_2~(\pm T_DD)\Bigl)\biggl) = 10`$

**Possible Combinations:** $`5^3*5^6*2^6*2=250~000~000`$  

*Case 5:  A(B(CD))*

$`T_{ABCD=100}\biggl((\pm T_AA)~O_0~\pm T_{BCD}\Bigl((\pm T_BB)~O_1~\pm T_{CD}\bigl((\pm T_CC)~O_2~(\pm T_DD)\bigl)\Bigl)\biggl) = 10`$

**Possible Combinations:** $`5^3*5^6*2^6*2=250~000~000`$ 

**Total Combinations: $`5*(5^3*5^6*2^6*2) + (5^3*5^4*2^4*2) = 1~252~500~000`$**

***With 10, 000 Number Combos:*  586 440 000 000**

# App Development:

- Vector Visualiser