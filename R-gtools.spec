#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-gtools
Version  : 3.5.0
Release  : 24
URL      : http://cran.r-project.org/src/contrib/gtools_3.5.0.tar.gz
Source0  : http://cran.r-project.org/src/contrib/gtools_3.5.0.tar.gz
Summary  : Various R Programming Tools
Group    : Development/Tools
License  : GPL-2.0
Requires: R-gtools-lib
BuildRequires : clr-R-helpers

%description
No detailed description available

%package lib
Summary: lib components for the R-gtools package.
Group: Libraries

%description lib
lib components for the R-gtools package.


%prep
%setup -q -c -n gtools

%build

%install
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --build  -l %{buildroot}/usr/lib64/R/library gtools
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library gtools


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/gtools/ChangeLog
/usr/lib64/R/library/gtools/DESCRIPTION
/usr/lib64/R/library/gtools/INDEX
/usr/lib64/R/library/gtools/Meta/Rd.rds
/usr/lib64/R/library/gtools/Meta/data.rds
/usr/lib64/R/library/gtools/Meta/hsearch.rds
/usr/lib64/R/library/gtools/Meta/links.rds
/usr/lib64/R/library/gtools/Meta/nsInfo.rds
/usr/lib64/R/library/gtools/Meta/package.rds
/usr/lib64/R/library/gtools/NAMESPACE
/usr/lib64/R/library/gtools/NEWS
/usr/lib64/R/library/gtools/R/gtools
/usr/lib64/R/library/gtools/R/gtools.rdb
/usr/lib64/R/library/gtools/R/gtools.rdx
/usr/lib64/R/library/gtools/data/ELISA.rda
/usr/lib64/R/library/gtools/help/AnIndex
/usr/lib64/R/library/gtools/help/aliases.rds
/usr/lib64/R/library/gtools/help/gtools.rdb
/usr/lib64/R/library/gtools/help/gtools.rdx
/usr/lib64/R/library/gtools/help/paths.rds
/usr/lib64/R/library/gtools/html/00Index.html
/usr/lib64/R/library/gtools/html/R.css
/usr/lib64/R/library/gtools/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/gtools/libs/gtools.so
