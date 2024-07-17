pkgname = "forgejo"
pkgver = "7.0.5"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_build_target = "all"
make_check_target = "test-backend"
make_use_env = True
hostmakedepends = ["gmake", "go", "nodejs"]
makedepends = ["linux-pam-devel"]
depends = ["git", "git-lfs"]
pkgdesc = "Git forge"
maintainer = "triallax <triallax@tutanota.com>"
license = "MIT"
url = "https://forgejo.org"
source = f"https://codeberg.org/forgejo/forgejo/archive/v{pkgver}.tar.gz"
sha256 = "9b949f1f501911e278a709d78c885c411ad76ed1031888d106fae539086ce021"
env = {
    "EXTRA_GOFLAGS": "-trimpath -buildmode=pie",
    "GITEA_VERSION": pkgver,
    # LDFLAGS is passed to go and not the c compiler, so override it
    "LDFLAGS": "-X 'code.gitea.io/gitea/modules/setting.AppWorkPath=/var/lib/forgejo/' -X 'code.gitea.io/gitea/modules/setting.CustomConf=/etc/forgejo/app.ini'",
    "TAGS": "bindata sqlite sqlite_unlock_notify pam",
}
# debug: fails to split on powerpc
# check: takes quite a bit
options = ["!debug", "!check"]


def post_prepare(self):
    from cbuild.util import golang

    golang.Golang(self).mod_download()

    self.log("installing npm dependencies...")
    self.do("npm", "ci", allow_network=True)


def init_build(self):
    from cbuild.util import golang

    self.make_env.update(golang.get_go_env(self))


def do_install(self):
    self.install_bin("gitea", name="forgejo")
    self.install_license("LICENSE")

    self.install_file(
        "custom/conf/app.example.ini", "usr/share/examples/forgejo"
    )
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_service(self.files_path / "forgejo")
