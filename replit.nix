{pkgs}: {
  deps = [
    pkgs.portaudio
    pkgs.ffmpeg
    pkgs.libsodium
    pkgs.libxcrypt
    pkgs.postgresql
    pkgs.openssl
  ];
}
