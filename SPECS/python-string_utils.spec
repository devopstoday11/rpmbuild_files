# which is only in Fedora 24+
%if 0%{?fedora} >= 24  || 0%{?rhel} >= 7
%global with_python3 1
%endif

%global library string_utils

Name:       python-%{library}
Version:    0.6.0
Release:    2%{?dist}
Summary:    A python module containing utility functions for strings 
License:    MIT
URL:        https://github.com/daveoncode/python-string-utils
Source0:    https://github.com/daveoncode/python-string-utils/%{library}-%{version}.tar.gz
BuildArch:  noarch

%package -n python2-%{library}
Summary:    A python module containing utility functions for strings 
%{?python_provide:%python_provide python2-%{library}}

BuildRequires: python2-devel
BuildRequires: python-setuptools
BuildRequires: git

Requires: python2

%description -n python2-%{library}
Python client for the kubernetes API.

%if 0%{?with_python3}
%package -n python3-%{library}
Summary: A python module containing utility functions for strings
%if 0%{?rhel}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{library}}
%else
%{?python_provide:%python_provide python3-%{library}}
%endif

%if 0%{?rhel}
BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-setuptools
%else
BuildRequires: python3-devel
BuildRequires: python3-setuptools
%endif
BuildRequires: git

%if 0%{?rhel}
Requires: python%{python3_pkgversion}
%else
Requires: python3
%endif

%description -n python3-%{library}
A python module containing utility functions for strings
%endif # with_python3

%description
A python module containing utility functions for strings

%prep
%autosetup -n %{library}-%{version} -S git

# Let's handle dependencies ourseleves

%build
%if 0%{?rhel}
%py_build
%else
%py2_build
%endif
%if 0%{?with_python3}
%py3_build
%endif

%install
%if 0%{?rhel}
%py_install
%else
%py2_install
%endif
%if 0%{?with_python3}
%py3_install
%endif
mkdir -p %buildroot/%_defaultdocdir/python2-string_utils
mkdir -p %buildroot/%_defaultdocdir/python3-string_utils
mv %buildroot/usr/README/README.md %buildroot/%_defaultdocdir/python2-string_utils
cp %buildroot/%_defaultdocdir/python2-string_utils/README.md %buildroot/%_defaultdocdir/python3-string_utils

%check

%files -n python2-%{library}
%license LICENSE
%if 0%{?rhel}
%doc %{_defaultdocdir}/python2-%{library}/README.md
%else
%doc README.md
%endif
%{python2_sitelib}/%{library}.*
%{python2_sitelib}/python_%{library}-*.egg-info

%if 0%{?with_python3}
%files -n python3-%{library}
%license LICENSE
%if 0%{?rhel}
%doc %{_defaultdocdir}/python3-%{library}/README.md
%else
%doc README.md
%endif

%{python3_sitelib}/%{library}.*
%{python3_sitelib}/__pycache__/%{library}.*
%{python3_sitelib}/python_%{library}-*.egg-info
%endif # with_python3

%changelog
* Wed May 10 2017 Jason Montleon <jmontleo@redhat.com> 0.6.0-2
- Fix python_provide for EL7 python3

* Wed May 10 2017 Jason Montleon <jmontleo@redhat.com> 0.6.0-1
- Initial Build

