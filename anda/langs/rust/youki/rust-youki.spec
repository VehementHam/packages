# Generated by rust2rpm 25
#bcond_without check

%global crate youki

Name:           rust-youki
Version:        0.3.0
Release:        %autorelease
Summary:        Container runtime written in Rust

License:        None
URL:            https://crates.io/crates/youki
Source:         %{crates_source}

BuildRequires:  anda-srpm-macros cargo-rpm-macros >= 24
BuildRequires:  pkg-config
BuildRequires:  systemd-devel
BuildRequires:  dbus-devel
BuildRequires:  libseccomp-devel
BuildRequires:  elfutils-libelf-devel
BuildRequires:  binutils

%global _description %{expand:
A container runtime written in Rust.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
License:        Apache-2.0

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE
%license LICENSE.dependencies
%doc README.md
%{_bindir}/youki

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep_online

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog