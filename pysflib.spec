%global         sum Python library used by the Software Factory project

Name:           pysflib
Version:        0.6.0
Release:        1%{?dist}
Summary:        %{sum}

License:        ASL 2.0
URL:            https://softwarefactory-project.io/r/p/%{name}
Source0:        https://github.com/redhat-cip/%{name}/archive/%{version}.tar.gz

BuildArch:      noarch

Requires:       python2-pygerrit
Requires:       python2-storyboardclient
Requires:       python2-redmine
Requires:       python-jenkins
Requires:       PyYAML
requires:       python-six

Buildrequires:  python2-devel
Buildrequires:  python-setuptools
Buildrequires:  python2-pbr
Buildrequires:  python-nose
Buildrequires:  python2-mock
BuildRequires:  python2-pygerrit
BuildRequires:  python2-storyboardclient
BuildRequires:  python2-redmine
BuildRequires:  python-jenkins
BuildRequires:  PyYAML
Buildrequires:  python-six

%description
Python library used by the Software Factory project to interact
with bundled services.

%package -n python2-pysflib
Summary:        %{sum}
Requires:       python2-pygerrit
Requires:       python2-storyboardclient
Requires:       python2-redmine
Requires:       python-jenkins
Requires:       PyYAML
requires:       python-six

Buildrequires:  python2-devel
Buildrequires:  python-setuptools
Buildrequires:  python2-pbr
Buildrequires:  python-nose
Buildrequires:  python2-mock
BuildRequires:  python2-pygerrit
BuildRequires:  python2-storyboardclient
BuildRequires:  python2-redmine
BuildRequires:  python-jenkins
BuildRequires:  PyYAML
Buildrequires:  python-six

%description -n python2-pysflib
Python library used by the Software Factory project to interact
with bundled services.

%prep
%autosetup -n %{name}-%{version}

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}

%check
nosetests -v

%files -n python2-pysflib
%{python2_sitelib}/*

%changelog
* Tue Feb 22 2017 Fabien Boucher <fboucher@redhat.com> - 1.0.0-1
- Initial packaging
