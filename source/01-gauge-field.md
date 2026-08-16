# Gauge field

## Generator convention

Conventions of the $SU(N_c)$ generators $T^a$, $a=1,\dots,N_c^2-1$, are taken in the anti-Hermitian, traceless, basis.

$$
\begin{aligned}
{T^a}^\dagger &= - T^a
\\
\mathrm{tr}\big(T^a T^b\big) &= -2 \, \delta^{ab}
\\
\mathrm{tr}\big(T^a\big) &= 0
\\
[T^a, T^b] &= 2 f^{abc} T^c
\\
T^a T^a &= - 2 \, \frac{N_c^2 - 1}{N_c} = - \frac{16}{3}
\quad (N_c = 3)
\end{aligned}
$$

## Gauge link and vector potential

The lattice degrees of freedom are the group-valued link variables $U_\mu(x) \in SU(N_c)$ attached to the directed link $(x, x+\hat\mu)$, with $U_\mu(x)^{-1} = U_\mu(x)^\dagger = U_{-\mu}(x+\hat\mu)$. They relate to the continuum color vector potential $\frac{1}{2} g A_\mu^a(x) T^a$ by the path-ordered exponential

$$
\begin{aligned}
U_\mu(x)
=&
\mathcal P \exp\Big( \int_x^{x+a \hat\mu} \mathrm{d} y \, \frac{1}{2} g A_\mu^a(y) \, T^a \Big)
\\
=&
\exp\big(\frac{1}{2} a g A_\mu^a(x) \, T^a\big)
+ \mathcal{O}(a^2)
\end{aligned}
$$

with lattice spacing $a$.

## Plaquette and field strength

The plaquette $U_P = U_{\mu\nu}(x)$ is the ordered product around an elementary square in the $(\mu,\nu)$ plane,

$$
\begin{aligned}
U_{\mu\nu}(x)
=&
U_\mu(x)\, U_\nu(x+\hat\mu)\,
U_\mu(x+\hat\nu)^\dagger\, U_\nu(x)^\dagger
\end{aligned}
$$

Expanding the links and using the Baker–Campbell–Hausdorff formula, the plaquette reproduces the field strength tensor

$$
\begin{aligned}
U_{\mu\nu}(x)
=&
1 + \frac{1}{2} a^2 g F_{\mu\nu}^a(x) \, T^a + \mathcal O(a^3)
\\
\frac{1}{N_c} \mathrm{tr}\big(U_{\mu\nu}(x)\big) - 1
=&
- \frac{1}{4} \frac{a^4 g^2}{N_c} \sum_{a} \big(F_{\mu\nu}^a(x)\big)^2 + \mathcal O(a^6)
\end{aligned}
$$

where

$$
\begin{aligned}
F_{\mu\nu}^a =& \partial_\mu A_\nu^a - \partial_\nu A_\mu^a + g f^{abc} A_\mu^b A_\nu^c
\end{aligned}
$$

## Gauge action

### Continuum

The Yang–Mills action in Euclidean space-time is

$$
\begin{aligned}
S_{\mathrm{YM}}
=&
- \frac{1}{8} \int \mathrm{d}^4 x \; \sum_{\mu,\nu,a,b} \mathrm{tr}\big(F_{\mu\nu}^a T^a \; F_{\mu\nu}^b T^b\big)
\\
=&
\frac{1}{4} \int \mathrm{d}^4 x \; \sum_{\mu,\nu,a} \big(F_{\mu\nu}^a\big)^2
\end{aligned}
$$

Here $g$ is the bare gauge coupling, related to the strong coupling by

$$
\begin{aligned}
\alpha_s = \frac{g^2}{4\pi}
\end{aligned}
$$

### Lattice (Wilson)

The Wilson gauge action is

$$
\begin{aligned}
S_{\mathrm{W}}
=&
- \beta \sum_{x,\,\mu < \nu}
\Big( \frac{1}{N_c} \mathrm{tr}\big(U_{\mu\nu}(x)\big) - 1 \Big)
\end{aligned}
$$

Relation to the continuum action can be obtained as

$$
\begin{aligned}
S_{\mathrm{W}}
=&
\frac{1}{4} \frac{\beta g^2}{N_c}
a^4 \sum_{x,\,\mu<\nu} \sum_a \big(F_{\mu\nu}^a\big)^2 + \mathcal O(a^2)
\\
&\xrightarrow{a\to0}
\frac{1}{8} \frac{\beta g^2}{N_c}
\int \mathrm{d}^4 x \; \sum_{\mu,\nu} \sum_a \big(F_{\mu\nu}^a\big)^2
\end{aligned}
$$

Requiring agreement with $S_{\mathrm{YM}}$ fixes the relation between the lattice parameter $\beta$ and the bare coupling, for $N_c = 3$,

$$
\begin{aligned}
\beta = \frac{2 N_c}{g^2},
\qquad
\beta = \frac{6}{g^2}
\quad (N_c = 3)
\end{aligned}
$$

so that $\beta \propto 1/g^2$ (continuum limit $\beta\to\infty$) and

$$
\begin{aligned}
\alpha_s = \frac{g^2}{4\pi} = \frac{3}{2\pi\, \beta}
\quad\text{for } N_c = 3
\end{aligned}
$$

A larger $\beta$ (weaker coupling) corresponds to a smoother gauge field and to the approach of the continuum limit; a smaller $\beta$ probes strong coupling.

### Symanzik-improved actions

The Wilson action can be improved by adding rectangular ($1\times2$ and $2\times1$) plaquettes. In the convention of the HMC source, the action with both parallelogram and $1\times2$ rectangle terms is parameterized by $c_1$,

$$
\begin{aligned}
S(U)
=&
- \beta \Big[
(1 - 8 c_1) \sum_P \big( \tfrac{1}{N_c} \mathrm{tr}(U_P) - 1 \big)
+ c_1 \sum_R \big( \tfrac{1}{N_c} \mathrm{tr}(U_R) - 1 \big)
\Big]
\end{aligned}
$$

The sums over $P$ and $R$ run only over the $(\mu<\nu)$ planes. Per site there are $6$ plaquettes; $12$ rectangles. A rectangle has twice the area of a plaquette. Since a loop's leading correction scales as the square of its area, each rectangle contributes $4$ times the leading deviation of a plaquette, so per plane the rectangle sum carries an effective weight $2 \times 4 = 8$. This is the origin of the $8 c_1$ in the coefficient $(1 - 8 c_1)$: the tree-level normalization $(1 - 8 c_1) + 8 c_1 = 1$ is independent of $c_1$.

Standard choices of $c_1$:

$$
\begin{aligned}
\text{Wilson:}\quad & c_1 = 0
\\
\text{Iwasaki:}\quad & c_1 = -0.331
\\
\text{DBW2:}\quad & c_1 = -1.4008
\end{aligned}
$$

## Summary

| Quantity | Symbol | Definition |
| --- | --- | --- |
| Gauge link | $U_\mu(x)$ | $\exp\big(\frac{1}{2} a g A_\mu^a T^a\big)$ |
| Vector potential | $A_\mu^a T^a$ | anti-Hermitian, $\mathrm{tr}(T^aT^b)=-2\delta^{ab}$ |
| Plaquette | $U_{\mu\nu}$ | ordered link product around $(\mu,\nu)$ square |
| Field strength | $F_{\mu\nu}^a$ | plaquette $U_{\mu\nu} =1+\frac{1}{2} a^2 g F_{\mu\nu}^a T^a+\dots$ |
| Lattice coupling | $\beta$ | $\beta = 2N_c/g^2 = 6/g^2$ ($SU(3)$) |
| Gauge coupling | $g$ | $\alpha_s = g^2/4\pi = 3/(2\pi\beta)$ |
| Wilson action | $S_{\mathrm W}$ | $-\beta\sum_P (\frac{1}{N_c}\mathrm{tr} U_P - 1)$ |
| Improved action | $S$ | Wilson $+\,c_1$ rectangle terms |
