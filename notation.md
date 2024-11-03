$$
\def\ba#1\ea{\begin{align}#1\end{align}}
\newcommand{\nn}{\nonumber}
\newcommand{\ra}{\rangle}
\newcommand{\la}{\langle}
\newcommand{\bra}{\big\rangle}
\newcommand{\bla}{\big\langle}
\newcommand{\Bra}{\Big\rangle}
\newcommand{\Bla}{\Big\langle}
\newcommand{\ud}{\mathrm{d}}
\newcommand{\a}{a}
\nn
$$

# Notation

## Common notation

$$
\ba
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
\sigma_x
=&
\left(
\begin{array}{cc}
1 & 0 \\
0 & -1\\
\end{array}
\right)
\ea
$$

$$
\ba
[\sigma_i,\sigma_j] = 2 i \epsilon_{i,j,k} \sigma_k
\ea
$$

$$
\ba
\epsilon_{x,y,z} = 1
\ea
$$

## Minkowski notation

Conventions follows "An Introduction To Quantum Field Theory" by Michael E. Peskin, Dan V. Schroeder.

https://www.amazon.com/Introduction-Quantum-Theory-Frontiers-Physics/dp/0201503972
$$
\ba
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
\ea
$$

$$
\ba
\epsilon^{t,x,y,z}
=&
1
\\
\epsilon_{t,x,y,z}
=&
-1
\ea
$$

Scalar propagator:
$$
\ba
G(x-y)
=&
\int \frac{d^4 p}{(2\pi)^4} \frac{i}{p^2 - m^2} e^{-i p\cdot (x-y)}
\ea
$$
Fermion related notations:
$$
\ba
\sigma^\mu
=&
(1, \vec \sigma)
\\
\bar\sigma^\mu
=&
(1, -\vec \sigma)
\ea
$$

$$
\ba
\gamma_\mu
=&
\left(
\begin{array}{cc}
0 & \sigma^\mu \\
\bar\sigma^\mu & 0\\
\end{array}
\right)
\ea
$$

Continuum free fermion action
$$
\ba
S=&
\int \bar\psi(x)(i \gamma^\mu\partial^x_\mu - m) \psi(x) d^4 x
\ea
$$
Free fermion propagator
$$
\ba
S^\textrm{Fermion}(x-y)
=&
\la T\big(\psi(x) \bar\psi(y)\big) \ra
\\
=&
\int \frac{d^4 p}{(2\pi)^4} \frac{i}{\gamma^\mu p_\mu - m} e^{-i p\cdot (x-y)}
\\
=&
\int \frac{d^4 p}{(2\pi)^4} i \frac{\gamma^\mu p_\mu + m}{p^2 - m^2} e^{-i p\cdot (x-y)}
\\
=&
(i\gamma^\mu \partial^x_\mu + m)G(x-y)
\ea
$$

$$
\ba
\gamma^\mu p_\mu + m
=&
\left(
\begin{array}{cc}
m & E - \vec p\cdot \vec \sigma \\
E + \vec p\cdot \vec \sigma & m\\
\end{array}
\right)
\ea
$$

$$
\ba
\gamma_5
=&
\left(
\begin{array}{cc}
-1 & 0 \\
0 & 1\\
\end{array}
\right)
=
i\gamma^t \gamma^x \gamma^y \gamma^z
\ea
$$

$$
\ba
P_R =& \frac{1 + \gamma_5}{2}
\\
P_L =& \frac{1 - \gamma_5}{2}
\ea
$$

$$
\ba
\psi_L =& P_L \psi
\\
\psi_R =& P_R \psi
\\
\bar\psi_L =& \bar\psi P_R
\\
\bar\psi_R =& \bar\psi P_L
\ea
$$

## Euclidean notation

$$
\ba
g_{\mu,\nu}
=
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
\ea
$$

$$
\ba
\epsilon_{x,y,z,t} = 1
\ea
$$

Scalar propagator:
$$
\ba
G(x-y)
=&
\int \frac{d^4 p}{(2\pi)^4} \frac{1}{p^2 + m^2} e^{i p\cdot (x-y)}
\\
=&
\frac{m \textrm{BesselK}(1, m\sqrt{(x-y)^2})}{4\pi^2\sqrt{(x-y)^2}}
\ea
$$
Fermion related notations:
$$
\ba
\sigma_\mu
=&
(i, \vec \sigma)
\ea
$$

$$
\ba
\gamma_\mu
=&
-i
\left(
\begin{array}{cc}
0 & \sigma_\mu \\
-\sigma_\mu^\dagger & 0\\
\end{array}
\right)
\ea
$$

Continuum free fermion action
$$
\ba
S=&
\int \bar\psi(x)(\gamma_\mu\partial^x_\mu + m) \psi(x) d^4 x
\ea
$$
Free fermion propagator
$$
\ba
S^\textrm{Fermion}(x-y)
=&
\la T\big(\psi(x) \bar\psi(y)\big) \ra
\\
=&
\int \frac{d^4 p}{(2\pi)^4} \frac{1}{i \gamma_\mu p_\mu + m} e^{i p\cdot (x-y)}
\\
=&
\int \frac{d^4 p}{(2\pi)^4} \frac{-i\gamma_\mu p_\mu + m}{p^2 + m^2} e^{i p\cdot (x-y)}
\\
=&
(-\gamma_\mu \partial^x_\mu + m)G(x-y)
\ea
$$

$$
\ba
-i\gamma_\mu p_\mu + m
=&
\left(
\begin{array}{cc}
m & E - \vec p\cdot \vec \sigma \\
E + \vec p\cdot \vec \sigma & m\\
\end{array}
\right)
\ea
$$

> Quote (https://en.wikipedia.org/wiki/Chirality_(physics)):
>
> The helicity of a particle is positive ("right-handed") if the direction of its spin is the same as the direction of its motion. It is negative ("left-handed") if the directions of spin and motion are opposite.

Based on the above definition, in the chiral limit where $m\to 0$, we can see that the upper two components represent left-handed fermion and the lower two components represent right-handed fermion. So we have:

$$
\ba
\gamma_5
=&
\left(
\begin{array}{cc}
-1 & 0 \\
0 & 1\\
\end{array}
\right)
=
\gamma_t \gamma_x \gamma_y \gamma_z 
\ea
$$

$$
\ba
P_R =& \frac{1 + \gamma_5}{2}
\\
P_L =& \frac{1 - \gamma_5}{2}
\ea
$$

$$
\ba
\psi_L =& P_L \psi
\\
\psi_R =& P_R \psi
\\
\bar\psi_L =& \bar\psi P_R
\\
\bar\psi_R =& \bar\psi P_L
\ea
$$

## Code notation

https://github.com/RBC-UKQCD/CPS_public

https://github.com/paboyle/Grid

https://github.com/lehner/gpt

https://github.com/jinluchang/Qlattice
$$
\ba
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
\right)
=
\gamma_x \gamma_y \gamma_z \gamma_t
\ea
$$
Note that the $\gamma_5$ matrix takes a different sign. This sign should be converted to the above Euclidean space when reporting the results.