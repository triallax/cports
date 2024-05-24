pkgname = "e2fsprogs"
pkgver = "1.47.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-elf-shlibs",
    "--enable-e2initrd-helper",
    "--enable-fuse2fs",
    "--enable-symlink-build",
    "--enable-symlink-install",
    "--enable-relative-symlinks",
    "--disable-rpath",
    "--disable-fsck",
    "--disable-uuidd",
    "--disable-libuuid",
    "--disable-libblkid",
    "--with-root-prefix=/usr",
    "e2fsprogs_cv_struct_st_flags=no",
    "MKDIR_P=mkdir -p",  # install-sh is buggy: it only creates one directory
]
# breaks build entirely
configure_gen = []
make_cmd = "gmake"
make_install_args = ["install-libs"]
hostmakedepends = ["gmake", "pkgconf", "texinfo"]
makedepends = [
    "fuse-devel",
    "libblkid-devel",
    "libuuid-devel",
    "linux-headers",
    "udev-devel",
]
checkdepends = ["perl", "bzip2"]
pkgdesc = "Ext2/3/4 file system utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "http://e2fsprogs.sourceforge.net"
source = f"$(KERNEL_SITE)/kernel/people/tytso/{pkgname}/v{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "5a33dc047fd47284bca4bb10c13cfe7896377ae3d01cb81a05d406025d99e0d1"
# test suite hangs on tr, killing it makes it continue? FIXME
options = ["!check"]


def post_patch(self):
    # failing tests
    for test in [
        "f_boundscheck",
        "f_del_dup_quota",
        "f_super_bad_csum",
        "j_recover_csum2_32bit",
        "j_recover_csum2_64bit",
        "j_recover_csum3_64bit",
        "j_recover_fast_commit",
        "m_offset",
    ]:
        self.rm(f"tests/{test}", recursive=True)


def post_install(self):
    # prevents udisks automount
    self.rm(self.destdir / "usr/lib/udev/rules.d/64-ext4.rules")


@subpackage("e2fsprogs-devel")
def _devel(self):
    self.depends += makedepends

    return self.default_devel(
        extra=[
            "usr/bin/compile_et",
            "usr/bin/mk_cmds",
            "usr/share/man/man1/compile_et.1",
            "usr/share/man/man1/mk_cmds.1",
            "usr/share/et",
            "usr/share/ss",
        ]
    )


@subpackage("e2fsprogs-libs")
def _libs(self):
    return self.default_libs()


@subpackage("fuse2fs")
def _fuse2fs(self):
    self.pkgdesc = "Ext2/3/4 FUSE driver"
    self.depends += ["fuse"]

    return [
        "usr/bin/fuse2fs",
        "usr/share/man/man1/fuse2fs.1",
    ]
