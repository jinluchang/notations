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

# Notation

## Common notation

$$
\begin{aligned}
\sigma_x
=&
\left(
\begin{array}{cc}
0 & 1 \\
1 & 0\\
\end{array}
\right)
\\
\sigma_y
=&
\left(
\begin{array}{cc}
0 & -i \\
i & 0\\
\end{array}
\right)
\\
\sigma_z
=&
\left(
\begin{array}{cc}
1 & 0 \\
0 & -1\\
\end{array}
\right)
\end{aligned}
$$

$$
\begin{aligned}
[\sigma_i,\sigma_j] = 2 i \epsilon_{i,j,k} \sigma_k
\end{aligned}
$$

$$
\begin{aligned}
\epsilon_{x,y,z} = 1
\end{aligned}
$$

## Minkowski notation

Conventions follows "An Introduction To Quantum Field Theory" by Michael E. Peskin, Dan V. Schroeder.

https://www.amazon.com/Introduction-Quantum-Theory-Frontiers-Physics/dp/0201503972

$$
\begin{aligned}
g_{\mu,\nu}
=&
\left(
\begin{array}{cccc}
1 & 0 & 0 & 0 \\
0 & -1 & 0 & 0\\
0 & 0 & -1 & 0\\
0 & 0 & 0 & -1\\
\end{array}
\right)
\end{aligned}
$$

$$
\begin{aligned}
\epsilon^{t,x,y,z}
=&
1
\\
\epsilon_{t,x,y,z}
=&
-1
\end{aligned}
$$

Scalar propagator:

$$
\begin{aligned}
G(x-y)
=&
\int \frac{d^4 p}{(2\pi)^4} \frac{i}{p^2 - m^2} e^{-i p\cdot (x-y)}
\end{aligned}
$$

Fermion related notations:

$$
\begin{aligned}
\sigma^\mu
=&
(1, \vec \sigma)
\\
\bar\sigma^\mu
=&
(1, -\vec \sigma)
\end{aligned}
$$

$$
\begin{aligned}
\gamma_\mu
=&
\left(
\begin{array}{cc}
0 & \sigma^\mu \\
\bar\sigma^\mu & 0\\
\end{array}
\right)
\end{aligned}
$$

Continuum free fermion action

$$
\begin{aligned}
S=&
\int \bar\psi(x)(i \gamma^\mu\partial^x_\mu - m) \psi(x) d^4 x
\end{aligned}
$$

Free fermion propagator

$$
\begin{aligned}
S^\textrm{Fermion}(x-y)
=&
\langle T\big(\psi(x) \bar\psi(y)\big) \rangle
\\
=&
\int \frac{d^4 p}{(2\pi)^4} \frac{i}{\gamma^\mu p_\mu - m} e^{-i p\cdot (x-y)}
\\
=&
\int \frac{d^4 p}{(2\pi)^4} i \frac{\gamma^\mu p_\mu + m}{p^2 - m^2} e^{-i p\cdot (x-y)}
\\
=&
(i\gamma^\mu \partial^x_\mu + m)G(x-y)
\end{aligned}
$$

$$
\begin{aligned}
\gamma^\mu p_\mu + m
=&
\left(
\begin{array}{cc}
m & E - \vec p\cdot \vec \sigma \\
E + \vec p\cdot \vec \sigma & m\\
\end{array}
\right)
\end{aligned}
$$

$$
\begin{aligned}
\gamma_5
=&
\left(
\begin{array}{cc}
-1 & 0 \\
0 & 1\\
\end{array}
\right) =
i\gamma^t \gamma^x \gamma^y \gamma^z
\end{aligned}
$$

$$
\begin{aligned}
P_R =& \frac{1 + \gamma_5}{2}
\\
P_L =& \frac{1 - \gamma_5}{2}
\end{aligned}
$$

$$
\begin{aligned}
\psi_L =& P_L \psi
\\
\psi_R =& P_R \psi
\\
\bar\psi_L =& \bar\psi P_R
\\
\bar\psi_R =& \bar\psi P_L
\end{aligned}
$$

## Euclidean notation

$$
\begin{aligned}
g_{\mu,\nu} =
\delta_{\mu,\nu}
=&
\left(
\begin{array}{cccc}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0\\
0 & 0 & 1 & 0\\
0 & 0 & 0 & 1\\
\end{array}
\right)
\end{aligned}
$$

$$
\begin{aligned}
\epsilon_{x,y,z,t} = 1
\end{aligned}
$$

Scalar propagator:

$$
\begin{aligned}
G(x-y)
=&
\int \frac{d^4 p}{(2\pi)^4} \frac{1}{p^2 + m^2} e^{i p\cdot (x-y)}
\\
=&
\frac{m \textrm{BesselK}(1, m\sqrt{(x-y)^2})}{4\pi^2\sqrt{(x-y)^2}}
\end{aligned}
$$

Some special cases:

$$
\begin{aligned}
G(x)
=&
\frac{1}{4\pi^2 x^2}
\quad
\text{if }
m=0
\end{aligned}
$$

$$
\begin{aligned}
G(x)
=&
\frac{\sqrt{2 \pi m |x|}}{8\pi^2 x^2} e^{-m|x|}
\quad
\text{if }
m|x| \gg 1
\end{aligned}
$$

Fermion related notations:

$$
\begin{aligned}
\sigma_\mu
=&
(i, \vec \sigma)
\end{aligned}
$$

$$
\begin{aligned}
\gamma_\mu
=&
-i
\left(
\begin{array}{cc}
0 & \sigma_\mu \\
-\sigma_\mu^\dagger & 0\\
\end{array}
\right)
\end{aligned}
$$

Continuum free fermion action

$$
\begin{aligned}
S=&
\int \bar\psi(x)(\gamma_\mu\partial^x_\mu + m) \psi(x) d^4 x
\end{aligned}
$$

Free fermion propagator

$$
\begin{aligned}
S^\textrm{Fermion}(x-y)
=&
\langle T\big(\psi(x) \bar\psi(y)\big) \rangle
\\
=&
\int \frac{d^4 p}{(2\pi)^4} \frac{1}{i \gamma_\mu p_\mu + m} e^{i p\cdot (x-y)}
\\
=&
\int \frac{d^4 p}{(2\pi)^4} \frac{-i\gamma_\mu p_\mu + m}{p^2 + m^2} e^{i p\cdot (x-y)}
\\
=&
(-\gamma_\mu \partial^x_\mu + m)G(x-y)
\end{aligned}
$$

$$
\begin{aligned}
-i\gamma_\mu p_\mu + m
=&
\left(
\begin{array}{cc}
m & E - \vec p\cdot \vec \sigma \\
E + \vec p\cdot \vec \sigma & m\\
\end{array}
\right)
\end{aligned}
$$

> Quote (https://en.wikipedia.org/wiki/Chirality_(physics)):
>
> The helicity of a particle is positive ("right-handed") if the direction of its spin is the same as the direction of its motion. It is negative ("left-handed") if the directions of spin and motion are opposite.

Based on the above definition, in the chiral limit where $m\to 0$, we can see that the upper two components represent left-handed fermion and the lower two components represent right-handed fermion. So we have:

$$
\begin{aligned}
\gamma_5
=&
\left(
\begin{array}{cc}
-1 & 0 \\
0 & 1\\
\end{array}
\right) =
\gamma_t \gamma_x \gamma_y \gamma_z 
\end{aligned}
$$

$$
\begin{aligned}
P_R =& \frac{1 + \gamma_5}{2}
\\
P_L =& \frac{1 - \gamma_5}{2}
\end{aligned}
$$

$$
\begin{aligned}
\psi_L =& P_L \psi
\\
\psi_R =& P_R \psi
\\
\bar\psi_L =& \bar\psi P_R
\\
\bar\psi_R =& \bar\psi P_L
\end{aligned}
$$

## Code notation

https://github.com/RBC-UKQCD/CPS_public

https://github.com/paboyle/Grid

https://github.com/lehner/gpt

https://github.com/jinluchang/Qlattice

$$
\begin{aligned}
\gamma_x
=&
i
\left(
\begin{array}{cc}
0 & \sigma_x \\
-\sigma_x & 0\\
\end{array}
\right)
\\
\gamma_y
=&
-i
\left(
\begin{array}{cc}
0 & \sigma_y \\
-\sigma_y & 0\\
\end{array}
\right)
\\
\gamma_z
=&
i
\left(
\begin{array}{cc}
0 & \sigma_z \\
-\sigma_z & 0\\
\end{array}
\right)
\\
\gamma_t
=&
\left(
\begin{array}{cc}
0 & 1 \\
1 & 0\\
\end{array}
\right)
\\
\gamma_5
=&
\left(
\begin{array}{cc}
1 & 0 \\
0 & -1\\
\end{array}
\right) =
\gamma_x \gamma_y \gamma_z \gamma_t
\end{aligned}
$$

The sign difference in $\gamma_x$ and $\gamma_z$ can be understood as a $180^\circ$ rotation around $y$ axis compared with the previous notation. To convert the two convention, we can use:

$$
\begin{aligned}
\left(
\begin{array}{cc}
\psi_L^\text{Eucl} \\
\psi_R^\text{Eucl} \\
\end{array}
\right) =& i
\left(
\begin{array}{cc}
\sigma_y & 0 \\
0 & \sigma_y\\
\end{array}
\right)
\left(
\begin{array}{cc}
\psi_L^\text{Code}  \\
\psi_R^\text{Code} \\
\end{array}
\right)
\\
\left(
\begin{array}{cc}
\psi_L^\text{Code}  \\
\psi_R^\text{Code} \\
\end{array}
\right) =& \frac{1}{i}
\left(
\begin{array}{cc}
\sigma_y & 0 \\
0 & \sigma_y\\
\end{array}
\right)
\left(
\begin{array}{cc}
\psi_L^\text{Eucl} \\
\psi_R^\text{Eucl} \\
\end{array}
\right)
\end{aligned}
$$

Or, we can keep the fermion spinor, but change the sign for all $\sigma_x$ and $\sigma_z$.

**Note** that, the $\gamma_5$ matrix in the code notation takes a different sign. This sign difference is not related to the above rotation. This sign should simply be changed back to the above Euclidean notation when reporting the final results.

We also define the following projection operators.

$$
\begin{aligned}
P_+ =& \frac{1 + \gamma_5}{2}
\\
P_- =& \frac{1 - \gamma_5}{2}
\end{aligned}
$$
