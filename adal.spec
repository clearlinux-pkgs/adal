#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : adal
Version  : 1.2.7
Release  : 24
URL      : https://files.pythonhosted.org/packages/90/d7/a829bc5e8ff28f82f9e2dc9b363f3b7b9c1194766d5a75105e3885bfa9a8/adal-1.2.7.tar.gz
Source0  : https://files.pythonhosted.org/packages/90/d7/a829bc5e8ff28f82f9e2dc9b363f3b7b9c1194766d5a75105e3885bfa9a8/adal-1.2.7.tar.gz
Summary  : Note: This library is already replaced by MSAL Python, available here: https://pypi.org/project/msal/ .ADAL Python remains available here as a legacy. The ADAL for Python library makes it easy for python application to authenticate to Azure Active Directory (AAD) in order to access AAD protected web resources.
Group    : Development/Tools
License  : MIT
Requires: adal-python = %{version}-%{release}
Requires: adal-python3 = %{version}-%{release}
Requires: PyJWT
Requires: cryptography
Requires: python-dateutil
Requires: requests
BuildRequires : PyJWT
BuildRequires : buildreq-distutils3
BuildRequires : cryptography
BuildRequires : python-dateutil
BuildRequires : requests

%description
This library, ADAL for Python, will no longer receive new feature improvements. Instead, use the new library

%package python
Summary: python components for the adal package.
Group: Default
Requires: adal-python3 = %{version}-%{release}

%description python
python components for the adal package.


%package python3
Summary: python3 components for the adal package.
Group: Default
Requires: python3-core
Provides: pypi(adal)
Requires: pypi(cryptography)
Requires: pypi(pyjwt)
Requires: pypi(python_dateutil)
Requires: pypi(requests)

%description python3
python3 components for the adal package.


%prep
%setup -q -n adal-1.2.7
cd %{_builddir}/adal-1.2.7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1617718479
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
