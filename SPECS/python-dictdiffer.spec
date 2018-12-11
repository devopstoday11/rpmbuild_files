%if 0%{?rhel} == 7
%bcond_with    python3
%bcond_without python2
%else
%bcond_with    python2
%bcond_without python3
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

%if 0%{?with_python2}
%package -n python2-%{library}
Summary:    Dictdiffer is a module that helps you to diff and patch dictionaries
%{?python_provide:%python_provide python2-%{library}}

BuildRequires: python2-devel
BuildRequires: python-pytest-runner
BuildRequires: python-setuptools
BuildRequires: git

Requires: python2

%description -n python2-%{library}
Dictdiffer is a module that helps you to diff and patch dictionaries
%endif # with python2

%if 0%{?with_python3}
%package -n python3-%{library}
Summary: Dictdiffer is a module that helps you to diff and patch dictionaries
%{?python_provide:%python_provide python3-%{library}}

BuildRequires: python3-devel
BuildRequires: python3-pytest-runner
BuildRequires: python3-setuptools
BuildRequires: git

Requires: python3

%description -n python3-%{library}
Dictdiffer is a module that helps you to diff and patch dictionaries
%endif # with_python3

#recommonmark not available for docs in EPEL
%if 0%{?fedora}
%package doc
Summary: Documentation for %{name}.
Provides: %{name}-%{version}-doc
%if 0%{?with_python3}
BuildRequires: python3-sphinx
BuildRequires: python3-recommonmark
%else
BuildRequires: python2-sphinx
BuildRequires: python2-recommonmark
%endif
%description doc
%{summary}
%endif

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
%if 0%{?with_python2}
%py2_build
%endif
%if 0%{?with_python3}
%py3_build
%endif

%if 0%{?fedora}
sphinx-build docs/ html
%{__rm} -rf html/.buildinfo
%endif

%install
%if 0%{?with_python2}
%py2_install
%endif
%if 0%{?with_python3}
%py3_install
%endif

%check

%if 0%{?with_python2}
%files -n python2-%{library}
%license LICENSE
%{python2_sitelib}/%{library}/*
%{python2_sitelib}/%{library}-*.egg-info
%endif

%if 0%{?with_python3}
%files -n python3-%{library}
%license LICENSE
%{python3_sitelib}/%{library}/*
%{python3_sitelib}/%{library}-*.egg-info
%endif

%if 0%{?fedora}
%files doc
%license LICENSE
%doc html
%endif

%changelog
* Tue Dec 4 2018 John Kim <jkim@redhat.com> 0.7.1-1
- Bump Versio to 0.7.1-1
- Fixed URL, Source0
- Enable disable python3 for rhel
- Add docs for fedora

* Wed May 10 2017 Jason Montleon <jmontleo@redhat.com> 0.6.1-1
- Initial Build
