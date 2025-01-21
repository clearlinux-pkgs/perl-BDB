#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v13
# autospec commit: dc0ff31b4314
#
Name     : perl-BDB
Version  : 1.92
Release  : 19
URL      : https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/BDB-1.92.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/BDB-1.92.tar.gz
Summary  : unknown
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-BDB-license = %{version}-%{release}
Requires: perl-BDB-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : db-dev
BuildRequires : perl(common::sense)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
BDB - Asynchronous Berkeley DB access
SYNOPSIS
use BDB;
my $env = db_env_create;

%package dev
Summary: dev components for the perl-BDB package.
Group: Development
Provides: perl-BDB-devel = %{version}-%{release}
Requires: perl-BDB = %{version}-%{release}

%description dev
dev components for the perl-BDB package.


%package license
Summary: license components for the perl-BDB package.
Group: Default

%description license
license components for the perl-BDB package.


%package perl
Summary: perl components for the perl-BDB package.
Group: Default
Requires: perl-BDB = %{version}-%{release}

%description perl
perl components for the perl-BDB package.


%prep
%setup -q -n BDB-1.92
cd %{_builddir}/BDB-1.92

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-BDB
cp %{_builddir}/BDB-%{version}/COPYING %{buildroot}/usr/share/package-licenses/perl-BDB/9a56f3b919dfc8fced3803e165a2e38de62646e5 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/BDB.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-BDB/9a56f3b919dfc8fced3803e165a2e38de62646e5

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
