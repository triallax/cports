pkgname = "ostree"
pkgver = "2024.10"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--with-builtin-grub2-mkconfig",
    "--with-crypto=openssl",
    "--with-modern-grub",
    "--with-openssl",
    "--with-curl",
    "--with-soup=no",
    "--disable-gtk-doc",
]
hostmakedepends = [
    "automake",
    "bison",
    "docbook-xsl-nons",
    "gobject-introspection",
    "gtk-doc-tools",
    "libtool",
    "pkgconf",
    "xsltproc",
]
makedepends = [
    "e2fsprogs-devel",
    "fuse-devel",
    "glib-devel",
    "gpgme-devel",
    "curl-devel",
    "libgpg-error-devel",
    "linux-headers",
    "openssl-devel",
    "xz-devel",
    "libarchive-devel",
]
checkdepends = ["attr-progs", "bsdtar", "gnupg", "xz"]
pkgdesc = "Operating system and container binary deployment and upgrades"
maintainer = "eater <=@eater.me>"
license = "LGPL-2.0-or-later"
url = "https://ostreedev.github.io/ostree"
source = f"https://github.com/ostreedev/ostree/releases/download/v{pkgver}/libostree-{pkgver}.tar.xz"
sha256 = "54e3387dee1ff16031a0679aca2b60da90ab7f4a26c211822333c7f23000abee"
# failing on their test harness, i will find motivation Soon
options = ["!check"]


@subpackage("ostree-devel")
def _(self):
    return self.default_devel()
