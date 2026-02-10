{ pkgs ? import <nixpkgs> {} }:

pkgs.callPackage ./notations.nix { }
