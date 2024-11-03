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

# Notation related to $\pi^0\to \gamma\gamma$

**Based on Euclidean notation (not the same as the $\gamma_5$ notation used in the code).**

The axial current that couple to $\pi^0$ is:

$$
\begin{align}
J_{\mu}^{5,\pi^0}(x) = \frac{1}{\sqrt 2}
\big(
\bar u(x) \gamma_\mu \gamma_5 u(x) -
\bar d(x) \gamma_\mu \gamma_5 d(x)
\big)
\end{align}
$$

The corresponding pseudo-scalar density

$$
\begin{align}
P^{\pi^0}(x) =
\frac{1}{\sqrt 2} \big(
\bar u(x) \gamma_5 u(x) -
\bar d(x) \gamma_5 d(x)
\big)
\end{align}
$$

We have ($p_t = i \sqrt{m_\pi^2 + \vec p^2 }$)

$$
\begin{align}
\langle 0 | i J_\mu^{5,\pi^0}(0) | \pi^0(\vec p) \rangle =
i f_\pi p_\mu
\end{align}
$$

$$
\begin{align}
\langle 0 | i P^{\pi^0}(0) | \pi^0(\vec p) \rangle
= f_\pi
\frac{m_\pi^2}{2 m_l}
\end{align}
$$

$$
\begin{align}
f_\pi = \sqrt 2 F_\pi
\end{align}
$$

$$
\begin{align}
\mathcal H_{\mu,\nu} (x, p)
=&
\langle 0 | T J_\mu(x/2) J_\nu(-x/2) | \pi(\vec p) \rangle
\\
=&
\epsilon_{\mu,\nu,\rho,\sigma}
x_\rho p_\sigma
H(x^2,p\cdot x)
\end{align}
$$

### OPE relation

At small $x$:

$$
\begin{align}
S^q(x)
=&
\langle T\{q(x) \bar q(0) \} \rangle
\\
\approx&
(-\gamma_\rho \partial_\rho + m_q) G(x)
\\
\approx&
\frac{2 x_\rho \gamma_\rho + m_q x^2}{4\pi^2 (x^2)^2}
\\
\end{align}
$$

$$
\begin{align}
\gamma_\mu \gamma_\rho\gamma_\nu =
-\epsilon_{\mu,\nu,\rho,\sigma} \gamma_\sigma \gamma_5
+
(
\delta_{\mu,\rho}\gamma_\nu
+\delta_{\rho,\nu}\gamma_\mu
-\delta_{\mu,\nu}\gamma_\rho
)
\end{align}
$$

$$
\begin{align}
T\{J_\mu(x) J_\nu(0)\}
=&
\sum_q
e_q^2
T(
\bar q(x) \gamma_\mu q(x)
\bar q(0) \gamma_\nu q(0)
)
\\
\simeq&
-\frac{1}{\pi^2(x^2)^2}
\epsilon_{\mu,\nu,\rho,\sigma}
x_\rho
\sum_q
e_q^2
\bar q(\frac{x}{2}) \gamma_\sigma \gamma_5 q(\frac{x}{2})
\end{align}
$$

$$
\begin{align}
\mathcal H_{\mu,\nu} (x, p)
\approx&
-\frac{1}{\pi^2(x^2)^2}
\epsilon_{\mu,\nu,\rho,\sigma}
x_\rho
\sum_q
e_q^2
\langle 0 | \bar q(0) \gamma_\sigma \gamma_5 q(0)  | \pi(\vec p) \rangle
\\
\approx& -
\frac{e_u^2 - e_d^2}{\pi^2}
\epsilon_{\mu,\nu,\rho,\sigma}
\frac{x_\rho}{(x^2)^2}
\frac{f_\pi}{\sqrt 2} p_\sigma
\end{align}
$$

Therefore:

$$
\begin{align}
H(x^2, p\cdot x)
\approx& -
\frac{e_u^2 - e_d^2}{\pi^2}
\frac{1}{(x^2)^2}
F_\pi
\end{align}
$$
