pkgname = "perl-io-tty"
pkgver = "1.18"
pkgrel = 0
build_style = "perl_module"
hostmakedepends = ["gmake", "perl"]
makedepends = ["perl"]
depends = ["perl"]
pkgdesc = "Low-level pseudo-tty allocation library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Artistic-1.0-Perl OR GPL-1.0-or-later"
url = "https://metacpan.org/release/IO-Tty"
source = f"$(CPAN_SITE)/IO/IO-Tty-{pkgver}.tar.gz"
sha256 = "b0e45b186e4ca54636b1f15111ec0fee86b993e23db529aacb4759df946792ff"
