{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = with pkgs; [
    python3
    python3Packages.pygame-ce  # pygame-ce has better Wayland/Niri support
    uv

    # Graphics libraries needed for the window to open
    libGL
    wayland
    libxkbcommon
    xorg.libX11
    xorg.libXcursor
    xorg.libXinerama
    xorg.libXext
    xorg.libXrandr
  ];

  shellHook = ''
    # This tells Pygame/SDL where to find the graphics drivers
    export LD_LIBRARY_PATH=${pkgs.libGL}/lib:${pkgs.libxkbcommon}/lib:${pkgs.wayland}/lib:$LD_LIBRARY_PATH
    
    # Force Pygame to use Wayland (since you are on Niri)
    export SDL_VIDEODRIVER=wayland
    
    # If Wayland fails, you can comment the line above and uncomment this for XWayland:
    # export SDL_VIDEODRIVER=x11
    
    echo "Asteroids dev environment loaded!"
  '';
}
