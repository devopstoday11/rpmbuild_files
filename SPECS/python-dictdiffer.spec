%if 0%{?fedora} >= 24  || 0%{?rhel} >= 7
%global with_python3 1
%endif

%global library dictdiffer

Name:       python-%{library}
Version:    0.7.1
Release:    1%{?dist}
Summary:    Dictdiffer is a module that helps you to diff and patch dictionaries 
License:    MIT
URL:        https://github.com/inveniosoftware/dictdiffer
Source0:    https://github.com/inveniosoftware/dictdiffer/archive/v%{version}.tar.gz
BuildArch:  noarch

%package -n python2-%{library}
Summary:    Dictdiffer is a module that helps you to diff and patch dictionaries 
%{?python_provide:%python_provide python2-%{library}}

BuildRequires: python2-devel
%if 0%{?fedora}
BuildRequires: python-pytest-runner
%endif
BuildRequires: python-setuptools
BuildRequires: git

Requires: python2

%description -n python2-%{library}
Python client for the kubernetes API.

%if 0%{?with_python3}
%package -n python3-%{library}
Summary: Dictdiffer is a module that helps you to diff and patch dictionaries
%if 0%{?rhel}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{library}}
%else
%{?python_provide:%python_provide python3-%{library}}
%endif

%if 0%{?rhel}
BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-pytest-runner
BuildRequires: python%{python3_pkgversion}-setuptools
%else
BuildRequires: python3-devel
BuildRequires: python3-pytest-runner
BuildRequires: python3-setuptools
%endif
BuildRequires: git

%if 0%{?rhel}
Requires: python%{python3_pkgversion}
%else
Requires: python3
%endif

%description -n python3-%{library}
Dictdiffer is a module that helps you to diff and patch dictionaries
%endif # with_python3

%description
Dictdiffer is a module that helps you to diff and patch dictionaries

%prep
%autosetup -n %{library}-%{version} -S git
# EL7 lacks python2-pytest-runner
%if 0%{?rhel}
sed -i -e /pytest-runner/d setup.py
%endif

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

%check

%files -n python2-%{library}
%license LICENSE
%{python2_sitelib}/%{library}/*
%{python2_sitelib}/%{library}-*.egg-info

%if 0%{?with_python3}
%files -n python3-%{library}
%license LICENSE
%{python3_sitelib}/%{library}/*
%{python3_sitelib}/%{library}-*.egg-info
%endif # with_python3

%changelog
* Wed May 10 2017 Jason Montleon <jmontleo@redhat.com> 0.6.1-1
- Initial Build

* Wed Dec 4 2018 John Kim <jkim@redhat.com> 0.7.1-1
- Bump Versio to 0.7.1-1
- Fixed URL, Source0
