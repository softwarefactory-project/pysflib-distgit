%global         sum Python library used by the Software Factory project

Name:           pysflib
Version:        0.7.0
Release:        3%{?dist}
Summary:        %{sum}

License:        ASL 2.0
URL:            https://softwarefactory-project.io/r/p/%{name}
Source0:        https://github.com/redhat-cip/%{name}/archive/%{version}.tar.gz

BuildArch:      noarch

Requires:       python2-storyboardclient
Requires:       PyYAML
Requires:       python-six

Buildrequires:  python2-devel
Buildrequires:  python-setuptools
Buildrequires:  python2-pbr
Buildrequires:  python-nose
Buildrequires:  python2-mock
BuildRequires:  python2-storyboardclient
BuildRequires:  PyYAML
Buildrequires:  python-six

%description
Python library used by the Software Factory project to interact
with bundled services.

%package -n python2-pysflib
Summary:        %{sum}
Requires:       python2-pygerrit
Requires:       python2-storyboardclient
Requires:       python-jenkins
Requires:       PyYAML
Requires:       python-six

Buildrequires:  python2-devel
Buildrequires:  python-setuptools
Buildrequires:  python2-pbr
Buildrequires:  python-nose
Buildrequires:  python2-mock
BuildRequires:  python2-pygerrit
BuildRequires:  python2-storyboardclient
BuildRequires:  python-jenkins
BuildRequires:  PyYAML
Buildrequires:  python-six

%description -n python2-pysflib
Python library used by the Software Factory project to interact
with bundled services.

%prep
%autosetup -n %{name}-%{version}

%build
export PBR_VERSION=%{version}
%{__python2} setup.py build

%install
export PBR_VERSION=%{version}
%{__python2} setup.py install --skip-build --root %{buildroot}

%check
nosetests -v

%files -n python2-pysflib
%{python2_sitelib}/*

%changelog
* Wed Apr 11 2017 Tristan Cacqueray <tdecacqu@redhat.com> - 0.7.0-3
- Remove dependency to pygerrit and python-jenkins

* Tue Mar 29 2017 Fabien Boucher <fboucher@redhat.com> - 0.7.0-2
- Remove dependency to pyton-redmine

* Fri Mar 10 2017 Tristan Cacqueray <tdecacqu@redhat.com> - 0.7.0-1
- Bump to 0.7.0

* Tue Feb 22 2017 Fabien Boucher <fboucher@redhat.com> - 1.0.0-1
- Initial packaging
