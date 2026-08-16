# Anomaly

**Based on Euclidean notation (not the same as the $\gamma_5$ notation used in the code).**

## PCAC relation

The partially conserved axial current (PCAC) relation for a single quark flavor $q$ follows from the axial-vector Ward–Takahashi identity. For a specific flavor define the axial current and pseudo-scalar density

$$
\begin{aligned}
J_\mu^{5,q}(x)
=&
\bar q(x) \gamma_\mu \gamma_5 q(x)
\\
P^{q}(x)
=&
\bar q(x) \gamma_5 q(x)
\end{aligned}
$$

The divergence of the axial current is not conserved in the presence of the $U(1)_A$ anomaly. Taking the anomaly into account, the (anomalous) PCAC relation for this flavor reads

$$
\begin{aligned}
\partial_\mu^{}
J_\mu^{5,q}(x)
=&
2 m_q \bar q(x) \gamma_5 q(x)
-
2 \, \rho_Q(x)
-
2\, N_c \, e_q^2 \, \rho_{\mathrm{em}}(x)
\end{aligned}
$$

where $\rho_Q(x)$ denotes the (color) topological charge density and $\rho_{\mathrm{em}}(x)$ the QED axial anomaly density, both defined below, and $m_q$ is the mass of the flavor $q$.

## Topological charge density

The topological charge density is defined in terms of the gauge field strength

$$
\begin{aligned}
\widetilde F_{\mu\nu}^a
=&
-\frac{1}{2} \epsilon_{\mu\nu\rho\sigma} F_{\rho\sigma}^a
\end{aligned}
$$

as

$$
\begin{aligned}
\rho_Q(x)
=&
\frac{g^2}{32\pi^2}
\, \sum_a F_{\mu\nu}^a(x) \widetilde F_{\mu\nu}^a(x)
\\
=&
- \frac{g^2}{64\pi^2}
\, \epsilon_{\mu\nu\rho\sigma}
\; \sum_a F_{\mu\nu}^a(x) F_{\rho\sigma}^a(x)
\end{aligned}
$$

Integrating over space-time gives the topological charge

$$
\begin{aligned}
Q
=
\int \mathrm{d}^4 x \, \rho_Q(x)
\end{aligned}
$$

which is an integer ($Q \in \mathbb Z$) on compact manifolds.

## QED axial anomaly density

In addition to the color anomaly, the axial current also couples to the electromagnetic (QED) field through the quark's electric charge. For a quark flavor $q$ carrying charge

$$
\begin{aligned}
e_q
=
\begin{cases}
+\tfrac{2}{3} & (u, c, t)
\\
-\tfrac{1}{3} & (d, s, b)
\end{cases}
\end{aligned}
$$

in units of the elementary charge $e$ (the positron charge), the axial current is obtained from the QCD current by replacing the covariant derivative with the electromagnetic one, $D_\mu \to D_\mu^{\mathrm{em}} = \partial_\mu + i\, e\, e_q A_\mu$, where $A_\mu$ denotes the (abelian) electromagnetic vector potential and the corresponding field strength is

$$
\begin{aligned}
F_{\mu\nu}
=&
\partial_\mu A_\nu - \partial_\nu A_\mu
\end{aligned}
$$

(the bare $F_{\mu\nu}$, $A_\mu$ without a color superscript are reserved for
QED).

$$
\begin{aligned}
\rho_{\mathrm{em}}(x)
=&
-\frac{e^2}{32\pi^2} \epsilon_{\mu\nu\rho\sigma}
\,
F_{\mu\nu}(x) F_{\rho\sigma}(x)
\end{aligned}
$$

is the QED axial anomaly density, defined in complete analogy with $\rho_Q$ but for the abelian field strength $F_{\mu\nu}$.  The factor $(e\, e_q)^2$ reflects the quark charge entering each of the two electromagnetic vertices of the triangle diagram; for the up quark $e_q^2 = 4/9$, for the down quark $e_q^2 = 1/9$. This QED part of the $U(1)_A$ anomaly is what underlies the anomalous decay $\pi^0 \to \gamma \gamma$.

## Index theorem connection

By the Atiyah–Singer index theorem, the topological charge equals the difference between numbers of left- and right-handed zero modes of the Dirac operator,

$$
\begin{aligned}
Q
=
n_L - n_R
\end{aligned}
$$

where $n_L$ and $n_R$ are the numbers of left- and right-handed zero modes of the (anti-Hermitian) Dirac operator $D$.

## Code notation

https://github.com/RBC-UKQCD/CPS_public

https://github.com/paboyle/Grid

https://github.com/lehner/gpt

https://github.com/jinluchang/Qlattice

**Note** that, the $Q$ in the code convention has the opposite sign as the definition above. This is related to the sign difference in the $\gamma_5$ convention in the code. The PCAC relation takes the same form in the code convention.
