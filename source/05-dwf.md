<!--
$$
\def\ba#1\ea{\begin{aligned}#1\end{aligned}}
\newcommand{\nn}{\nonumber}
\newcommand{\ra}{\rangle}
\newcommand{\la}{\langle}
\newcommand{\bra}{\big\rangle}
\newcommand{\bla}{\big\langle}
\newcommand{\Bra}{\Big\rangle}
\newcommand{\Bla}{\Big\langle}
\newcommand{\ud}{\mathrm{d}}
\nn
$$
-->

# Domain wall fermion

**Based on Code notation (not the same as the Euclidean $\gamma_5$ defined before).**

Domain wall fermion formulation introduces the fifth dimension, which label as $s$. The action is

$$
\begin{aligned}
S_F^\text{DWF}
=&
\sum_{x,s;x',s'}
\bar\psi(x,s)
D_\text{DWF}(x,s;x',s')
\psi(x',s')
\\
D^\text{DWF}_m(x,s;x',s')
=&
\Big(\delta(x-x')+D^\text{W}_{-M_5}(x;x')\Big)
\delta(s-s')
\nonumber\\&
-
m(s) P_+ \delta(s-s'-1)
-
m(s') P_- \delta(s-s'+1)
\\
D^\text{W}_{-M_5}(x;x')
=&
(4-M_5) \delta(x-x')
\nonumber\\&
-\frac{1}{2}\sum_\mu\Big(
(1-\gamma_\mu)U_\mu(x)\delta(x+\mu-x')
\nonumber\\&\hspace{1.5cm}
+
(1+\gamma_\mu)U^{-1}_\mu(x')\delta(x-\mu-x')
\Big)
\\
m(s)
=&
-m\delta(s)
+1-\delta(s)
\end{aligned}
$$

where $x,x'$ represent space time coordinates of lattice sites, and $s,s'$ represent the coordinates in the fifth dimension, range from $0$ to $L_s-1$ ($L_s$ sites in the fifth dimension). All the components of the coordinates are integers.

