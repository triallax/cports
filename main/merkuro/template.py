pkgname = "merkuro"
pkgver = "25.04.3"
pkgrel = 0
build_style = "cmake"
make_check_args = ["-E", "akonadi-sqlite-.*"]
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "akonadi-calendar-devel",
    "akonadi-contacts-devel",
    "akonadi-devel",
    "akonadi-search-devel",
    "gpgme-devel",
    "kcalendarcore-devel",
    "kcalutils-devel",
    "kconfigwidgets-devel",
    "kcontacts-devel",
    "kcoreaddons-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "kholidays-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kidentitymanagement-devel",
    "kio-devel",
    "kirigami-addons-devel",
    "kirigami-devel",
    "kitemmodels-devel",
    "kmailtransport-devel",
    "kmime-devel",
    "knotifications-devel",
    "kwindowsystem-devel",
    "libplasma-devel",
    "mailcommon-devel",
    "messagelib-devel",
    "mimetreeparser-devel",
    "pimcommon-devel",
    "qqc2-desktop-style-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtlocation-devel",
    "qt6-qtsvg-devel",
]
depends = [
    "kdepim-runtime",
    "kirigami-addons",
    "qt6-qt5compat",
    "qt6-qtlocation",
]
checkdepends = ["xwayland-run", *depends]
pkgdesc = "KDE calendar with cloud sync"
license = "LGPL-3.0-only AND GPL-3.0-or-later"
url = "https://apps.kde.org/merkuro.calendar"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/merkuro-{pkgver}.tar.xz"
sha256 = "c213e7f4bd746e699ec56315cd26393124283e9190a5e9c2c3adf21811cdde27"
