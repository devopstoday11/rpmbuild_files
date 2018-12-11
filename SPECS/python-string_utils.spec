%if 0%{?rhel} == 7
%bcond_with    python3
%bcond_without python2
%else
%bcond_with    python2
%bcond_without python3
%endif

%global library string_utils

Name:       python-%{library}
Version:    0.6.0
Release:    2%{?dist}
Summary:    A python module containing utility functions for strings
License:    MIT
URL:        https://github.com/daveoncode/python-string-utils
Source0:    https://github.com/daveoncode/python-string-utils/archive/v%{version}.tar.gz
BuildArch:  noarch

%if 0%{?with_python2}
%package -n python2-%{library}
Summary:    A python module containing utility functions for strings
%{?python_provide:%python_provide python2-%{library}}

BuildRequires: python2-devel
BuildRequires: python-setuptools
BuildRequires: git

Requires: python2

%description -n python2-%{library}
A python module containing utility functions for strings
%endif # with python2

%if 0%{?with_python3}
%package -n python3-%{library}
Summary: A python module containing utility functions for strings
%{?python_provide:%python_provide python3-%{library}}

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: git

Requires: python3

%description -n python3-%{library}
A python module containing utility functions for strings
%endif # with_python3

%description
A python module containing utility functions for strings

%prep
%autosetup -n python-string-utils-%{version} -S git

# Let's handle dependencies ourseleves

%build
%if 0%{?with_python2}
%py2_build
%endif
%if 0%{?with_python3}
%py3_build
%endif

%install
%if 0%{?with_python2}
%py2_install
mkdir -p %buildroot/%_defaultdocdir/python2-string_utils
mv %buildroot/usr/README/README.md %buildroot/%_defaultdocdir/python2-%{library}
%endif

%if 0%{?with_python3}
%py3_install
mkdir -p %buildroot/%_defaultdocdir/python3-string_utils
mv %buildroot/usr/README/README.md %buildroot/%_defaultdocdir/python3-%{library}
%endif

%check

%if 0%{?with_python2}
%files -n python2-%{library}
%license LICENSE
%doc %{_defaultdocdir}/python2-%{library}/README.md
%{python2_sitelib}/%{library}.*
%{python2_sitelib}/python_%{library}-*.egg-info
%endif

%if 0%{?with_python3}
%files -n python3-%{library}
%license LICENSE
%doc %{_defaultdocdir}/python3-%{library}/README.md
%{python3_sitelib}/%{library}.*
%{python3_sitelib}/__pycache__/%{library}.*
%{python3_sitelib}/python_%{library}-*.egg-info
%endif # with_python3

%changelog
* Tue Dec 4 2018 John Kim <jkim@redhat.com> 0.6.0-3
- Fixed URL, Source0
- Enable disable python3 for rhel

* Wed May 10 2017 Jason Montleon <jmontleo@redhat.com> 0.6.0-2
- Fix python_provide for EL7 python3

* Wed May 10 2017 Jason Montleon <jmontleo@redhat.com> 0.6.0-1
- Initial Build
