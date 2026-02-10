{
  version ? "25.11",
  pkgs ? import (fetchTarball "https://channels.nixos.org/nixos-${version}/nixexprs.tar.xz") {},
}:

pkgs.callPackage ./notations.nix { }
