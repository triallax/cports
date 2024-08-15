pkgname = "gamescope"
pkgver = "3.14.29"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Ddefault_library=static",
    "-Davif_screenshots=enabled",
    "-Ddrm_backend=enabled",
    "-Dinput_emulation=enabled",
    "-Dpipewire=enabled",
    "-Drt_cap=enabled",
    "-Dsdl2_backend=enabled",
]
make_install_args = ["--skip-subprojects", "libliftoff,openvr,vkroots,wlroots"]
hostmakedepends = [
    "cmake",
    "glslang-progs",
    "libcap-progs",
    "meson",
    "ninja",
    "pkgconf",
    "spirv-headers",
]
makedepends = [
    "benchmark-devel",
    "glm",
    "glslang-devel",
    "hwdata-devel",
    "libavif-devel",
    "libcap-devel",
    "libdisplay-info-devel",
    "libei-devel",
    "libinput-devel",
    "libseat-devel",
    "libx11-devel",
    "libxcomposite-devel",
    "libxdamage-devel",
    "libxmu-devel",
    "libxrender-devel",
    "libxres-devel",
    "libxtst-devel",
    "libxxf86vm-devel",
    "pipewire-devel",
    "pixman-devel",
    "sdl-devel",
    "stb",
    "vulkan-headers",
    "vulkan-loader-devel",
    "wayland-protocols",
    "xcb-util-wm-devel",
    "xwayland-devel",
]
pkgdesc = "SteamOS compositor"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://github.com/ValveSoftware/gamescope"
source = [
    f"{url}/archive/refs/tags/{pkgver}.tar.gz",
    "https://github.com/ValveSoftware/openvr/archive/ebd425331229365dc3ec42d1bb8b2cc3c2332f81.tar.gz",
    "https://github.com/Joshua-Ashton/vkroots/archive/5106d8a0df95de66cc58dc1ea37e69c99afc9540.tar.gz",
    "https://gitlab.freedesktop.org/wlroots/wlroots/-/archive/4666996b2a34b53899aedafcd3586fb1c7a16af6.tar.gz",
    "https://gitlab.freedesktop.org/emersion/libliftoff/-/archive/8b08dc1c14fd019cc90ddabe34ad16596b0691f4.tar.gz",
    "https://github.com/Joshua-Ashton/reshade/archive/696b14cd6006ae9ca174e6164450619ace043283.tar.gz",
]
source_paths = [
    ".",
    "subprojects/openvr",
    "subprojects/vkroots",
    "subprojects/wlroots",
    "subprojects/libliftoff",
    "src/reshade",
]
sha256 = [
    "e4d50ab4419760d2f52203a06184b31366b672a1d34d72f3e51d9ff3cdf56507",
    "c1913dbd1f3218b113ca7921d8cf9a1c1ddd28b432452c236cdd027dfbd7a95b",
    "37b77586e91f7ebee70380dcddd73bf01ae4acef1053e6be41d0485ede022422",
    "83d95c49caa8bf92019428ae0b5e59804d5d662c2589b0cc8c39fe4029267bde",
    "8de28aee6f90f47b7fc7037dcd2360166197c0b5d2033f3afdbd34f2ea1bf216",
    "3aa6feda7773cc8ffa8fb012fe95e6207c776101e29198d0e0d34a0c5e339f6a",
]
file_modes = {
    "usr/bin/gamescope": ("root", "root", 0o755),
}
file_xattrs = {
    "usr/bin/gamescope": {
        "security.capability": "cap_sys_nice+ep",
    },
}
# sus
options = ["!cross"]

tool_flags = {"CXXFLAGS": ["-DRTLD_DEEPBIND=0"]}


def post_install(self):
    self.install_license("LICENSE")
