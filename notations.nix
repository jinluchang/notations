{ stdenv
, lib
, sphinx
, python3Packages
, rsync
, ... 
}:

stdenv.mkDerivation rec {
  pname = "notations";
  version = "1.0";

  src = ./.;

  nativeBuildInputs = [
    sphinx
    python3Packages.linkify-it-py
    python3Packages.myst-parser
    rsync
  ];

  buildPhase = ''
    runHook preBuild
    echo "Building documentation..."
    make html
    runHook postBuild
  '';

  installPhase = ''
    runHook preInstall
    mkdir -p "$out/share/doc/${pname}/"
    rsync -a --delete ./build/ "$out/share/doc/${pname}/"
    mkdir -pv "$out"/share/version
    echo "${version}" > "$out/share/version/${pname}"
    runHook postInstall
  '';

  meta = with lib; {
    description = "Documentation for Notations";
    license = licenses.gpl3;
  };
}
