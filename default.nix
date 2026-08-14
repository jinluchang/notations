{
  version ? "26.05",
  pkgs ? import (fetchTarball "https://channels.nixos.org/nixos-${version}/nixexprs.tar.xz") {},
}:

pkgs.callPackage ./notations.nix { }
